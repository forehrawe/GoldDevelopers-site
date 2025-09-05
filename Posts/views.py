from django.shortcuts import render
from django.views import View
from .models import Posts

# Create your views here.
class Posts(View):
    def get(self, request, id):
        
        return render(request, 'Posts.html')