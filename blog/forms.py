from django import forms
from django.contrib.auth.models import User
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['published_date','author','created_date']
        fileds = ['title','text']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control','rows':4}),
        }


class UserForm(forms.ModelForm):
    #password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class UserLoginForm(forms.Form):
    #password = forms.CharField(widget = forms.PasswordInput)
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
