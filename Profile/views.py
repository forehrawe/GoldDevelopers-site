from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from Homepage.models import PostsModel


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