from django.contrib.auth import authenticate, login, forms
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic, View

from .forms import UserRegisterForm

from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.


class SignUpView(View):
    template_name = 'accounts/signup.html'

    def get(self, request):
        context = {
            'form': UserRegisterForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

