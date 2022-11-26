from django.db import models
from user.models import User

class Draft(models.Model):
    style = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.style
    
class Style(models.Model):
    image = models.ImageField(upload_to='style/')
    
    def __str__(self):
        return self.image

class Size(models.Model):
    draft = models.ForeignKey(Draft,on_delete=models.CASCADE, related_name='draft_set')
    size = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return (f"{self.draft}, {self.size}")

class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    draft = models.ForeignKey(Draft,on_delete=models.CASCADE, null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='result/', max_length=255, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="user_likes")