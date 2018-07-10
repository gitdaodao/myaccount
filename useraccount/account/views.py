from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'account/dashboard.html')



def login(request):
    return render(request,'account/login.html')