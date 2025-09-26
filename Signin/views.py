from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.
class Signin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/profile')
        else:
            return render(request, 'signin.html')
    
    def post(self, request):
        User = get_user_model()
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
            return redirect("/")
        except:
            return render(request, "signin.html", {'response_result':'Invalid Username Or Password'})