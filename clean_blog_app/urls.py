from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name="index"),
    path('single_post/<int:id>', views.SinglePost, name="single"),
]
