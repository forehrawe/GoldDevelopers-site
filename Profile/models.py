from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfileModel(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    verified_status = models.CharField(max_length=20)
    
    def __str__(self):
        return self.account.username