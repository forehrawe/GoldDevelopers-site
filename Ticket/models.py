from django.db import models
from datetime import datetime
# Create your models here.
class Tickets(models.Model):
    sender_email = models.EmailField()
    content = models.CharField(max_length=300)
    time = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.sender_email