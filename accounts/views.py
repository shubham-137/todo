from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    
    if request.method=='POST':
        password = request.POST.get('psw')
        username = request.POST.get('username')
        user=auth.authenticate(username=username,password=password)
        print("ddddd")
        if user is not None:
            print("fff")
            auth.login(request,user)
            
            return redirect('tasks/')
            # return render(request,'todo.html')

        else:
            print("eee")
            messages.info(request,'invalid credentials')
            return redirect('login')    

    else:
        return render(request,'login.html') 







def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')
        username = request.POST.get('username')
        password1=request.POST.get('psw-repeat')
        
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('/')
            else:
                user=User.objects.create_user(email=email,password=password,username=username)
                user.save()
                
                return redirect('login')
        else:
            messages.info(request,'password not matching')  
            return redirect('/')      
        return redirect('/')



    else:
        return render(request,'register.html')    

def logout(request):
    auth.logout(request)
    return redirect('/')
            
