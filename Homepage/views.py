from django.views.generic import ListView
from .models import Posts

# Create your views here.
class Homepage(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name = 'posts'