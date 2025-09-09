from django.db import models

# Create your models here.
class PostsModel(models.Model):
    Author = models.CharField(max_length=30)
    Title = models.CharField(max_length=40)
    Summary = models.TextField(default='')
    Date = models.DateField(auto_now_add=True)
    Content = models.TextField()
    JustDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Title
    
class Documentations(models.Model):
    JustDate = models.DateTimeField(auto_now_add=True)
    Date = models.DateField(auto_now_add=True)
    Title = models.CharField(max_length=30)
    Content_p1 = models.CharField(max_length=700)
    Content_p2 = models.CharField(max_length=700)
    Content_p3 = models.CharField(max_length=700)
    Content_p4 = models.CharField(max_length=700)
    
    def __str__(self):
        return self.Title
