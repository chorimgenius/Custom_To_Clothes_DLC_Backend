from django.urls import path
from article import views

urlpatterns = [
    path('', views.RankArticleView.as_view(), name='order_view'),
]