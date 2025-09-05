from django.urls import path
from Homepage.views import Homepage

urlpatterns = [
    path('', Homepage.as_view(), name='Homepage-Named')
]
