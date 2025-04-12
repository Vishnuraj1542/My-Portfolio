from django.urls import path
from .views import *



urlpatterns=[
    path('',Home.as_view(),name='homepage'),
    path('contact/',Contact.as_view(),name='contact_page'),
    path('skills/',Skill.as_view(),name='skillspage'),
    path('projects/',Project.as_view(),name='projects'),
    path('football/',Football,name='footballsite'),
    path('education/',Education,name='education')
]