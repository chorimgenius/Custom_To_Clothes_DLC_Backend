from django.db import models
from article.models import Size
from article.models import Article
from user.models import User

# Create your models here.
class Order(models.Model):
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mount = models.IntegerField()
    status = models.IntegerField()