from django.urls import path
from order import views

urlpatterns = [
    path('<int:article_id>/', views.OrderView.as_view(), name='order_view'),
    path('cart/', views.CartView.as_view(), name='cart_view'),
    path('list/', views.OrderListView.as_view(), name='orderlist_view'),
]
