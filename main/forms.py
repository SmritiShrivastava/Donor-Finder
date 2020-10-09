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
    confirm_Password = forms.CharField(max_length = 100)

class logInForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(max_length = 100)

class donorForm(forms.Form):
    donated = forms.BooleanField()
    drinked = forms.BooleanField()
    disease = forms.BooleanField()

class searchForm(forms.Form):
    search = forms.CharField(max_length=100)