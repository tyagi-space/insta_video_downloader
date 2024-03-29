from django.shortcuts import render
from basic_app.form import UserForm,UserProfileInfoForm
from basic_app.form import URLinputForm
from basic_app import downloader
# Create your views here.

def index(request):
    got = False
    if request.method == 'POST':
        url_value = URLinputForm(data=request.POST)
        if url_value.is_valid():
            #print(url_value.cleaned_data['inputURL']) 
            value = url_value.save()
            stringval = value.inputURL_value
            downloader.get_response(stringval)
            got = True
         
    else:
        url_value = URLinputForm()
    return render(request,'basic_app/index.html',{'url_value':url_value,'got':got})

# def register(request):
#     registered = False

#     if request.method == 'POST':
#         user_form = UserForm(data = request.POST)
#         profile_form = UserProfileInfoForm(data=request.POST)

#         if user_form.is_valid() and profile_form.is_valid():

#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']

#             profile.save()

#             registered = True
#         else:
#             print(user_form.errors,profile_form.errors)

#     else:
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()

#     return render(request,'basic_app/registration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'basic_app/registration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})
