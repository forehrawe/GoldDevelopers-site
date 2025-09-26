from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth import login, get_user_model
from profile.models import ProfileModel

# Create your views here.
class Signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/profile')
        else:
            form = CustomUserCreationForm()
            return render(request, 'signup.html', {'form':form})
    
    def post(self, request):
        response_result = None
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            user_obj = User.objects.filter(email=request.POST.get('email')).exists()
            if not user_obj:
                user = form.save()
                login(request, user) 
                verified_email = ProfileModel(verified_status='bi bi-x-circle', account = user)
                verified_email.save()
                return redirect("/")
            else:
                response_result = 'This Email Exists!'
        return render(request, 'signup.html', {'form': form, 'response_result':response_result})
