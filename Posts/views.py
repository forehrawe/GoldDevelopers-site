from django.shortcuts import render, get_object_or_404
from django.views import View
from homepage.models import PostsModel

# Create your views here.
class Posts(View):
    def get(self, request, id):
        obj = get_object_or_404(PostsModel, id=id)
        return render(request, 'Posts.html', {'obj':obj})