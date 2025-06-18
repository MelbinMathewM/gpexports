from django.shortcuts import render
from user_app.models import quote
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def Home_page(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        exports=quote.objects.create(fullname=fullname,email=email,phone=phone,message=message)
        exports.save()
        
        # Send email notification
        subject = f"New Quote from {fullname}"
        body = f"""
        A new quote has been submitted:

        Full Name: {fullname}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            ['gpexports05@gmail.com','george.prince.chemparathickal@gmail.com'],
            fail_silently=False,
        )
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