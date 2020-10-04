from django import forms

class signUpForm(forms.Form):
    username = forms.CharField(max_length = 200)
    firstName = forms.CharField(max_length = 200)
    lastName = forms.CharField(max_length = 200)
    bloodGroup = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=50)
    age = forms.IntegerField()
    contactNumber = forms.IntegerField()
    password = forms.CharField(max_length = 100)
    confirmPassword = forms.CharField(max_length = 100)

class logInForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(max_length = 100)