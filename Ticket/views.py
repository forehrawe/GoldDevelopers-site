from django.shortcuts import render
from django.views import View
from .models import Tickets
from django.utils import timezone
import telebot
from profile.models import ProfileModel

class Ticket(View):
    def get(self, request):
        return render(request, 'ticket.html')
    
    def post(self, request):
        
        user_id = request.user.id
        v_status = ProfileModel.objects.get(id=user_id)
        
        if v_status == 'bi bi-check-circle':
        
            TOKEN = "7699562921:AAEPX_vy9a7JLbvqDGWWtdiR9CMOB0p9nT0"
            bot = telebot.TeleBot(TOKEN)
            
            message = None
            email = request.user.email
            last_ticket = Tickets.objects.filter(sender_email=email).order_by('-time').first()
            
            if last_ticket: 
                now = timezone.now()
                delta = now - last_ticket.time
                if delta.days < 1:
                    message = {'message':'شما امروز یک تیکت ثبت کرده اید فردا امتحان کنید.'}
                    return render(request, 'ticket.html', message)
                else:
                    subject = request.POST.get('category')
                    content = request.POST.get('content')
                    bot.send_message(6673359808, f'Email: {email} \n\n\n subject: {subject} \n\n {content}  \n\n\n {request.user.id}')
                    message = 'پیام شما ارسال شد و از طریق ایمیل به آن پاسخ داده خواهد شد'
                    database_conn = Tickets(sender_email=email, content=content)
                    database_conn.save()
                    return render(request, 'ticket.html', {'message':message})
                    
            else:
                subject = request.POST.get('category')
                content = request.POST.get('content')
                bot.send_message(6673359808, f'Email: {email} \n\n\n subject: {subject} \n\n {content}  \n\n\n\n user_id : {request.user.id}')
                message = 'پیام شما ارسال شد و از طریق ایمیل به آن پاسخ داده خواهد شد'
                database_conn = Tickets(sender_email=email, content=content)
                database_conn.save()
                return render(request, 'ticket.html', {'message':message})

        else:
            message = 'برای ارسال تیکت باید ایمیل خود را تایید کنید'
            return render(request, 'ticket.html', {'message':message})