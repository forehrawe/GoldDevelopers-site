from django.urls import path
from .views import Verify

urlpatterns = [
    path('', Verify.as_view())
]
