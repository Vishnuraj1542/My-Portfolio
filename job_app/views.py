from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from django.conf import settings

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'base.html')

class Skill(View):
    def get(self,request):
        return render(request,'skills.html')
    

class Contact(View):
    def get(self,request):
        return render(request,'contact.html')
    def post(self,request):
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save()
            subject=f"A new message from {contact.name} "
            message= f"{contact.message} Email: {contact.email}"
            send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER],fail_silently=False)
            return HttpResponse('''<script>alert("Thankyou sir ");window.location=""</script>''')
        return render(request,'contact.html',{'from':form})


class Project(View):
    def get(self,request):
        return render(request,'project.html')

def Football(request):
    return render(request,'football.html')

def Education(request):
    return render(request,'education.html')