from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from profile.models import ProfileModel
from django.core.mail import send_mail
import random
import hashlib
from profile.models import ProfileModel

# Create your views here.
class Verify(View):
    def send_code(self, request):
        chars = list('1234567890')
        code = ''.join(random.choices(chars, k=6))
        self.code_hex = hashlib.sha256(code.encode()).hexdigest()
        request.session['code_hex'] = self.code_hex
        subject = "verification Code"
        message = code
        rec_list = [request.user.email]
        send_mail(subject=subject, message=message, from_email=None, recipient_list=rec_list)
        del code
        
    
    def get(self, request):
        if request.user.is_authenticated:
            verified_obj = ProfileModel.objects.get(id=request.user.id)
            
            if verified_obj.verified_status == 'bi bi-check-circle':
                return redirect('/profile')
            
            
                

            return render(request, 'verify.html')
        
        else:
            return redirect('/signin')
        
    def post(self, request):
        status = request.POST.get('status')
        if status == 'sendcode':
            self.send_code(request)
            
        if status == 'verifycode':
            code = request.POST.get('code')
            code_hex = hashlib.sha256(code.encode()).hexdigest()
            
            if code_hex == request.session.get('code_hex'):
                verified_obj = ProfileModel.objects.get(id=request.user.id)
                verified_obj.verified_status = 'bi bi-check-circle'
                verified_obj.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'failed'})
            
            
        return render(request, 'verify.html')