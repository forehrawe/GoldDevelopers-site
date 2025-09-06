from django.urls import path
from .views import Profile, Logout

urlpatterns = [
    path('', Profile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout')
]
