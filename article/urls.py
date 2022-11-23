from django.urls import path
from article import views

urlpatterns = [
    path('article/', views.CustomView.as_view())
]