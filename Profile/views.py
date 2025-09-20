from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth import logout
from .models import ProfileModel
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.utils import IntegrityError


class Profile(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            
            context = {
                'user': user,
            }
            return render(request, 'profile.html', context)
        else:
            return redirect('/signin')
            
        
        
class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')
        else:
            return HttpResponse('You Are Not In Account.')
    
    

class ProfileEdit(View):
    def get(self, request):
        if request.user.is_authenticated:
            profile = ProfileModel.objects.get(account=request.user)
            user = request.user
            context = { 
                'user': user,
                'profile':profile
            }
            return render(request, 'profileEdit.html', context)
        else: 
            return redirect('/signin')
        
    def post(self, request):
        if request.user.is_authenticated:
            message = {}
            
            user = request.user
            if request.POST.get('username') == user.username:
                message['username'] = 'تغییری در یوزرنیم ایجاد نشد.'
            else:
                new_username = request.POST.get('username').strip()
                if new_username:
                    try:
                        user = User.objects.get(id=request.user.id)
                        user.username = request.POST.get('username')
                        user.save()
                        message['username'] = 'یوزرنیم با موفقیت تغییر کرد.'
                    except IntegrityError as e:
                        if e.args[0] == 1062:
                            message['username'] = 'این یوزرنیم قبلا ایجاد شده!'
                else:
                    message['username'] = 'یوزرنیم نمیتواند خالی باشد.'
                
            if request.POST.get('email') == user.email:
                message['email'] = 'تغییری در ایمیل ایجاد نشد.'
            else:
                new_email = request.POST.get('email').strip()
                if new_email:
                    user = User.objects.get(id=request.user.id)
                    user.email = request.POST.get('email')
                    user.save()
                    message['email'] = 'ایمیل با موفقیت تغییر کرد.'
                    profileVerificationStatus = ProfileModel.objects.get(account=request.user)
                    profileVerificationStatus.verified_status = 'bi bi-x-circle'
                    profileVerificationStatus.save()
                else:
                    message['email'] = 'ایمیل نمیتواند خالی باشد'
                    
            profile = ProfileModel.objects.get(account=request.user)
            message['profile'] = {
                'verified_status':profile.verified_status
            }
            return JsonResponse({'message': message})
                
        else:
            return redirect('/signin')
                    
                    