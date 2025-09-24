from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from profile.models import ProfileModel
from django.core.mail import send_mail
import random
import hashlib

# Create your views here.
class Verify(View):
    def sned_code(self, request):
        chars = list('1234567890')
        code = ''.join(random.choices(chars, k=6))
        self.code_hex = hashlib.sha256(code.encode()).hexdigest()
        subject = "verification Code"
        message = code
        rec_list = [request.user.email]
        send_mail(subject=subject, message=message, from_email=None, recipient_list=rec_list)
        
    
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'verify.html')
        
        else:
            return redirect('/signin')
        
    def post(self, request):
        status = request.POST.get('status')
        if status == 'sendcode':
            pass
            
            