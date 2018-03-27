from django import forms
from django.core import validators
from django.contrib.auth.models import User
from voltageapi import models
from . import models as viewmodel

class voltapiform(forms.ModelForm):
    class Meta():
        model =models.monthly_accumulate
        fields='__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = viewmodel.UserProfileInfo
        fields = ('portfolio_site','profile_pic')







# def check_for_z(value):
#     if value[0].lower() !=0:
#         raise forms.ValidationError("Name should be Z")


# class FormName(forms.Form):
#     #name = forms.CharField(validators=[check_for_z])
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email =forms.EmailField(label="Enter your email Again")
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher =forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email= all_clean_data['email']
#         vmail = all_clean_data['verify_email']
#
#         if email!=vmail:
#             raise forms.ValidationError("emails don't match")
    #def clean_botcatch(self):
        #botchatcher = self.cleaned_data['botcatcher']
        #if len(botchatcher)>0 :
    #        raise forms.ValidationError('Gotchya')
    #    return botchatcher
