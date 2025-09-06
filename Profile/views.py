from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from Homepage.models import PostsModel


class Profile(View):
    def get(self, request):
        user = request.user
        posts_count = PostsModel.objects.filter(Author=user).count()
        context = {
            'user': user,
            'posts_count': posts_count,
        }
        return render(request, 'profile.html', context)
        
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')