from django.urls import path
from homepage.views import Homepage

urlpatterns = [
    path('', Homepage.as_view(), name='Homepage-Named')
]
