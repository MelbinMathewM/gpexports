from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache

from user_app.models import quote
# Create your views here.
def register_user(request):
    
    return render(request,'register_user.html')


def quotes(request):
    all=quote.objects.all()
    return render(request,'quote.html',{'view':all})


def feedback(request):
    return render(request,'feedback.html')



def login_admin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            request.session['username'] = user.username

            return  redirect('register_user')
        else:
            return render(request,'login_admin.html',{'error':'Invalid Username and Password'})
           
    return render(request,'login_admin.html')



@never_cache
def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect('Home_page')
