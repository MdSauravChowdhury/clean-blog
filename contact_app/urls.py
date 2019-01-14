from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact_us, name="contact"),
    path('about/', views.teamAbout, name="about"),
]
