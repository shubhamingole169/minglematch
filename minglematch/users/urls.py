# users/urls.py
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]

# users/views.py
from django.shortcuts import render
from allauth.account.views import SignupView
from .forms import CustomSignupForm

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

register = CustomSignupView.as_view()
