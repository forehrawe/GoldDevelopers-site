from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from Homepage.models import PostsModel
from .models import ProfileModel


class Profile(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            
            context = {
                'user': user,
            }
            return render(request, 'profile.html', context)
        else:
            return redirect('/signin')
            
        
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
    
    
    
class ProfileEdit(View):
    def get(self, request):
        if request.user.is_authenticated:
            profile = ProfileModel.objects.get(account=request.user)
            user = request.user
            context = { 
                'user': user,
                'profile':profile
            }
            return render(request, 'profileEdit.html', context)
        else: 
            return redirect('/signin')