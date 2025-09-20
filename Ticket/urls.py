from django.urls import path
from .views import Ticket

urlpatterns = [
    path('', Ticket.as_view(), name='ticket')
]
