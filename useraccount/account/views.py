from django.shortcuts import render,redirect,reverse
from .forms import LoginForm,UserRegForm,UserForm,ProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
# 第三种方案 settings.py 同意匹配地址后 @login_required(login_url='/account/login/') 这个()可以省略了
#第二方案 @login_required(login_url='/account/login/')
@login_required(login_url='/account/login/')
def dashboard(request):
    """用户中心"""
    # 第一种限制未授权用户登录
    # if not request.user.is_authenticated:
    #     return redirect(reverse('account:login'))
    return render(request,'account/dashboard.html')



def user_login(request):
    """用户登录"""
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


def user_logout(request):
    logout(request)
    return redirect(reverse('account:login'))


def user_reg(request):
    """新用户注册"""
    if request.method=='POST':
        new_form=UserRegForm(request.POST)
        if new_form.is_valid():
            u=new_form.save(commit=False)
            u.set_password(new_form.cleaned_data['password'])
            u.save()
            return render(request,'account/register_done.html',{'new_user':u})
    else:
        new_form=UserRegForm()
    return render(request,'account/register.html',{'new_form':new_form})

def edit(request):
    """用户编辑"""
    if request.method=='POST':
        user_form=UserForm(instance=request.user,data=request.POST)
        profile_form=ProfileForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form })