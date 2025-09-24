from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('database-managements/', admin.site.urls),
    path('', include('homepage.urls')),
    path('signin/', include('signin.urls')),
    path('post/', include('posts.urls')),
    path('signup/', include('signup.urls')),
    path('profile/', include('profile.urls')),
    path('ticket/', include('ticket.urls')),
    path('verifyaccount/', include('verify.urls')),
]


#handler404 = 'error_handler.views.custom_404'