from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from order.serializers import OrderSerializer, OrderViewSerializer
from .models import Article
from .models import Size


# clothes_page
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
            size = Size.objects.get(draft_id=article.draft_id, size=request.data["size"])
            serializer.save(article_id=article_id, size=size, user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
