from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from Profile.models import ProfileModel
# Create your views here.
class Signup(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form':form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, "Account Created Successfully!")
            verified_email = ProfileModel(verified_status='bi bi-x-circle', account = user)
            verified_email.save()
            return redirect("/")
        return render(request, 'signup.html', {'form': form})
