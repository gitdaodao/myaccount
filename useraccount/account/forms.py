from django import forms 

class LoginForm(forms.Form):
    """用户登录"""
    username=forms.CharField(label='用户名',max_length=15)
    password=forms.CharField(label='密码',widget=forms.PasswordInput)
