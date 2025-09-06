from django.views.generic import ListView
from .models import PostsModel

# Create your views here.
class Homepage(ListView):
    model = PostsModel
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-JustDate']