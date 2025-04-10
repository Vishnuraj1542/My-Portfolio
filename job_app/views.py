from django.shortcuts import render,redirect
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'base.html')

class Contact(View):
    def get(self,request):
        return render(request,'contact.html')

class Skill(View):
    def get(self,request):
        return render(request,'skills.html')
