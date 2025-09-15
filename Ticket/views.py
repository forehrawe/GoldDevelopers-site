from django.shortcuts import render
from django.views import View
from .models import Tickets
from datetime import datetime
import telebot

class Ticket(View):
    def get(self, request):
        return render(request, 'ticket.html')
    
    def post(self, request):
        TOKEN = "7699562921:AAEPX_vy9a7JLbvqDGWWtdiR9CMOB0p9nT0"
        bot = telebot.TeleBot(TOKEN)
        
        message = None
        email = request.user.email
        last_ticket = Tickets.objects.filter(sender_email=email).order_by('-time').first()
        
        if last_ticket: 
            now = datetime.now()
            delta = now - last_ticket.time
            if delta.days < 1:
                message = {'message':'شما امروز یک تیکت ثبت کرده اید فردا امتحان کنید.'}
                return render(request, 'ticket.html', message)
            else:
                subject = request.POST.get('category')
                content = request.POST.get('content')
                bot.send_message(6673359808, f'subject: {subject} \n \n {content}')
                message = 'پیام شما ارسال شد و از طریق ایمیل به آن پاسخ داده خواهد شد'
                database_conn = Tickets(sender_email=email, content=content)
                database_conn.save()
                return render(request, 'ticket.html', {'message':message})
                
        else:
            subject = request.POST.get('category')
            content = request.POST.get('content')
            bot.send_message(6673359808, f'subject: {subject} \n \n {content}')
            message = 'پیام شما ارسال شد و از طریق ایمیل به آن پاسخ داده خواهد شد'
            database_conn = Tickets(sender_email=email, content=content)
            database_conn.save()
            return render(request, 'ticket.html', {'message':message})