from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from order.serializers import OrderSerializer, OrderViewSerializer, CartViewSerializer, OrderListViewSerializer

from .models import Article
from .models import Size
from .models import Order

#clothes_profile
class OrderView(APIView):
    def get(self, request, article_id):
         article = Article.objects.get(id=article_id)
         article_serializer = OrderViewSerializer(article)
         print(article_serializer)
         return Response(article_serializer.data, status=status.HTTP_200_OK)
     
    def post(self, request, article_id): 
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            article = Article.objects.get(id=article_id) 
            size = Size.objects.get(draft_id=article.draft_id, id=request.data["size"]) 
            serializer.save(article_id=article_id, size=size, user=request.user) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#cart (image, size, mount, price)   
class CartView(APIView):
    def get(self, request): 
        order = Order.objects.filter(user=request.user)
        print(order)
        cart_serializer = CartViewSerializer(order, many=True)
        print(cart_serializer)
        return Response(cart_serializer.data, status=status.HTTP_200_OK)

#orderlist(size, mount, price, status)
class OrderListView(APIView):
    def get(self, request): 
        order = Order.objects.filter(user=request.user)
        orderlist_serializer = OrderListViewSerializer(order, many=True)
        print(orderlist_serializer)
        return Response(orderlist_serializer.data, status=status.HTTP_200_OK)

        
