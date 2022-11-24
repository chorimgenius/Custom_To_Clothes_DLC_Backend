from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from article.models import Draft
from article.models import Style
from article.models import Article
from article.serializers import CustomViewSerializer
from article.serializers import CustomStyleViewSerializer
from article.serializers import ArticlePostSerializer
from article.serializers import ArticleSerializer
from article.serializers import ArticlePutSerializer
from django.db.models import Count
from uuid import uuid4
import os


class CustomView(APIView):
    def get(self,request):
        draft = Draft.objects.all()
        serializer = CustomViewSerializer(draft, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CustomStyleViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        image_uuid = uuid4().hex # 머신러닝 결과 파일 이름
        base_image = Draft.objects.get(id=request.data['draft']).image.name # draft image 이름
        style_image = serializer.data['image'][1:] # style image 이름

        os.system('python style-transfer-pytorch/style_transfer/cli.py media/'+ base_image +' '+ style_image +' -s 156 -ii 1 -o media/temp/'+ image_uuid +'.png') # style-transfer-pytorch
        os.system('rembg i media/temp/'+ image_uuid +'.png media/result/'+ image_uuid +'.png') # 누끼

        article = Article()
        article.user = request.user
        article.draft = Draft.objects.get(id=request.data['draft'])
        article.style_id = serializer.data['id']
        article.image = 'result/' + image_uuid + '.png'
        article.save()

        article_serializer = ArticlePostSerializer(article)
        return Response(article_serializer.data, status=status.HTTP_200_OK)
            

    
    def put(self,request):
        serializer = CustomStyleViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        image_uuid = uuid4().hex # 머신러닝 결과 파일 이름
        base_image = Draft.objects.get(id=request.data['draft']).image.name # draft image 이름
        style_image = serializer.data['image'][1:] # style image 이름
        
        style_transfer_pytorch = 'python style-transfer-pytorch/style_transfer/cli.py media/'+ base_image +' '+ style_image +' -s 156 -ii 1 -o media/temp/'+ image_uuid +'.png'
        rembg_cli = 'rembg i media/temp/'+ image_uuid +'.png media/result/'+ image_uuid +'.png'
        os.system(style_transfer_pytorch)
        os.system(rembg_cli)

        article = Article.objects.get(id=request.data['id'])
        serializer_put = ArticlePutSerializer(article,data=request.data)
        
        if serializer_put.is_valid():
            serializer_put.save(image = 'result/' + image_uuid + '.png', style_id = serializer.data['id'])
        else:
            return Response(serializer_put.errors, status=status.HTTP_400_BAD_REQUEST)
        
        article_serializer = ArticlePostSerializer(article)
        return Response(article_serializer.data, status=status.HTTP_200_OK)
        

class RankArticleView(APIView):
    def get(self, request):
        article = Article.objects.annotate(like_count = Count('likes')).order_by('-like_count')
        print(article)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
