from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        txt1 = request.POST['username']
        txt2 = request.POST['first']
        txt3 = request.POST['last']
        txt4 = request.POST['email']
        txt5 = request.POST['password']
        txt6 = request.POST['password1']

        if txt5 == txt6:
            if User.objects.filter(username=txt1).exists():
                messages.info(request,"username taken")
                return redirect('register')

            elif User.objects.filter(email=txt4).exists():
                messages.info(request,"Email already exist!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=txt1,password=txt5,first_name=txt2,last_name=txt3,email=txt4)

            user.save();
            return redirect('login')
            print("user created")
        else:
            messages.info(request,"password not match")
            return redirect('register')

        return redirect('/')

    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
