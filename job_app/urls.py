from django.urls import path
from .views import *



urlpatterns=[
    path('',Home.as_view(),name='homepage'),
    path('contact/',Contact.as_view(),name='contact_page')
]