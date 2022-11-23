from django.urls import path
from order import views

urlpatterns = [
    path('<int:article_id>/', views.OrderView.as_view(), name='order_view'),
]
