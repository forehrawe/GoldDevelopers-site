from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login
# Create your views here.
class Signup(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form':form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()                  # ذخیره کاربر در دیتابیس
            login(request, user)                # کاربر اتومات وارد سایت میشه
            messages.success(request, "Account Created Successfully!")
            return redirect("/")
        return render(request, 'signup.html', {'form': form})
