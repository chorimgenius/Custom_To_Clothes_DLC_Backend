from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('article.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
]
