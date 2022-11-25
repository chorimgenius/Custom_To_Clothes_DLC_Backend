from django.db import models
from user.models import User

class Draft(models.Model):
    style = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.style
    
class Style(models.Model):
    image = models.ImageField(upload_to='style/')

class Size(models.Model):
    draft = models.ForeignKey(Draft,on_delete=models.CASCADE, related_name='draft_set')
    size = models.CharField(max_length=50)
    stock = models.IntegerField(default=999)
    price = models.IntegerField()
    color = models.CharField(max_length=50)

class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    draft = models.ForeignKey(Draft,on_delete=models.CASCADE, null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='result/', max_length=255, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="user_likes")