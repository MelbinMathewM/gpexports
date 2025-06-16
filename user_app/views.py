from django.shortcuts import render
from user_app.models import quote
# Create your views here.


def Home_page(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        exports=quote.objects.create(fullname=fullname,email=email,phone=phone,message=message)
        exports.save()
    return render(request,'Home_page.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact_us(request):
    return render(request,'contact_us.html')

def gallery(request):
    return render(request,'gallery.html')

def error(request):
    return render(request,'error.html')