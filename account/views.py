from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import CreateView
from django.urls import  reverse_lazy
# Create your views here.

class SignUp(CreateView):
    template_name = 'account/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('account:login')
