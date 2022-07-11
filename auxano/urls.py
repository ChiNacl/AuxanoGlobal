from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sermon/', views.sermon, name='sermon'),
    path('partnership/', views.partnership, name='partnership'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('contact/contact_process/', views.contact, name='contactp'),
]
