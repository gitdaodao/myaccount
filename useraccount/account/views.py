from django.shortcuts import render,redirect,reverse
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request,'account/dashboard.html')



def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            username=data['username']
            pwd=data['password']
            # 用户验证  易错user.is_active 不带()
            user=authenticate(username=username,password=pwd)
            if user:
                if user.is_active:
                    # 验证成功后用户标示
                    login(request,user)
                    return redirect(reverse('account:dashboard'))
                else:
                    return HttpResponse('用户被锁定')
            else:
                return HttpResponse('用户名或者密码错误请重试~')
    form=LoginForm()
    return render(request,'account/login.html',{"form":form })