from django.urls import path
from .views import Posts

urlpatterns = [
    path('<int:id>/', Posts.as_view())
]
