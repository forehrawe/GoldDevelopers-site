from django.db import models

# Create your models here.
class Tickets(models.Model):
    sender_email = models.EmailField()
    content = models.CharField(max_length=300)
    
    def __str__(self):
        return self.sender_email