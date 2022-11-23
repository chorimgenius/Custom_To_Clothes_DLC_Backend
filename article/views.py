from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from article.serializers import ArticleSerializer
from article.models import Article
from django.db.models import Count

# Create your views here.
class RankArticleView(APIView):
    def get(self, request):
        article = Article.objects.annotate(like_count = Count('likes')).order_by('-like_count')
        print(article)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)