from django import forms
from .models import userModel

class userForm(forms.ModelForm):
    class Meta:
        model = userModel
        fields = ['username','email','contact','dob','password','cpassword','gender','address']

