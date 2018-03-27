from django.shortcuts import render
from voltageapi.models import measurement
from . import forms
from voltageview.forms import voltapiform,UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#@login_required
def index(request):
    #measurements= measurement.objects.all()
    print("hi")
    return render(request,"voltageview/index.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('voltage_view:index'))

@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required
def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic= request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'voltageview/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})
@login_required
def VoltapiForm(request):

    form= voltapiform()

    if request.method == "POST":
        form = voltapiform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error")
    return render(request,'voltageview/formindex.html',{'form':form})


def user_login(request):

    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('voltage_view:index'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Some one tried to login and failed")
            return HttpResponse("Invalid credentials")

    else:
        print("last else")
        return render(request,'voltageview/login.html',{})


# def form_name_view(request):
#     form = forms.FormName()
#
#     if request.method == "POST":
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             print("Validation Success")
#             print("Name is"+form.cleaned_data['name'])
#             print("Email is"+form.cleaned_data['email'])
#             print("Text is"+form.cleaned_data['text'])
#
#     return render(request,'voltageview/formindex.html',{'form':form})
