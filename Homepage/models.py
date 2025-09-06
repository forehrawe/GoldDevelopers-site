from django.db import models

# Create your models here.
class PostsModel(models.Model):
    Author = models.CharField(max_length=30)
    Title = models.CharField(max_length=40)
    Summary = models.TextField(default='')
    Content = models.TextField()
    
    def __str__(self):
        return self.Title