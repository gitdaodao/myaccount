from django import forms 
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    """用户登录"""
    username=forms.CharField(label='用户名',max_length=15)
    password=forms.CharField(label='密码',widget=forms.PasswordInput)


class UserRegForm(forms.ModelForm):
    """依据已有User类模型 造自己需要的用户注册表单"""
    password=forms.CharField(label='密码',max_length=21,widget=forms.PasswordInput)
    re_password=forms.CharField(label='重复密码',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','email','first_name')

    def cl_re_password(self):
        data=self.cleaned_data
        if data['password'] != data['re_password']:
            raise forms.ValidationError('两次输入的密码不一致')
        return data['re_password']


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','first_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('mobile','photo')