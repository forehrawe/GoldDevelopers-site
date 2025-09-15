from django.urls import path
from .views import Profile, Logout, ProfileEdit

urlpatterns = [
    path('', Profile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile-edit/', ProfileEdit.as_view(), name='ProfileEdit')
]
