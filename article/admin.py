from django.contrib import admin
from .models import Article
from .models import Draft
from .models import Size
# Register your models here.
admin.site.register(Article)
admin.site.register(Draft)
admin.site.register(Size)