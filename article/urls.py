from django.urls import path
from article import views

urlpatterns = [
    path('article/', views.CustomView.as_view()),
    path('', views.RankArticleView.as_view(), name='order_view'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='ClothesLike'),
]