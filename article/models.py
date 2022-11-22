from django.db import models

# Create your models here.
class Draft(models.Model):
    style = models.CharField(max_length=50)
    image = models.TextField()

class Size(models.Model):
    draft = models.ForeignKey(Draft,on_delete=models.CASCADE, related_name='draft_set')
    size = models.CharField(max_length=50)
    stock = models.IntegerField(default=999)
    price = models.IntegerField()
    color = models.CharField(max_length=50)

