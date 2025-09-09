from django.shortcuts import render
from django.views import View
from .models import Tickets

class Ticket(View):
    def get(self, request):
        return render(request, 'ticket.html')
    
    def post(self, request):
        email = request.user.email
        subject = request.POST.get('category')
        last_email = Tickets.objects.filter(sender=email)
        print(last_email)
        message = 'پیام شما ارسال شد و از طریق ایمیل به آن پاسخ داده خواهد شد'
        return render(request, 'ticket.html', {'message':message})