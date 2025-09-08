from django.shortcuts import render
from django.views.generic import TemplateView

class Ticket(TemplateView):
    template_name = 'ticket.html'