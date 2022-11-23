from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from article.models import Draft
from article.models import Style
from article.serializers import CustomViewSerializer
from article.serializers import CustomStyleViewSerializer
from article.serializers import ArticlePostSerializer
from article.models import Article
import os
from uuid import uuid4
from PIL import Image
from django.core.files import File


class CustomView(APIView):
    def get(self,request):
        draft = Draft.objects.all()
        serializer = CustomViewSerializer(draft, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CustomStyleViewSerializer(data=request.data)
        article = Article()
        if serializer.is_valid():
            serializer.save()

        article.user = request.user
        article.style_id = serializer.data['id']
        
        image_uuid = uuid4().hex
        image_draft = Draft.objects.get(id=request.data['draft']).image.name
        print(image_draft)
        print(serializer.data)
        os.system('python style-transfer-pytorch/style_transfer/cli.py media/'+ image_draft +' '+ serializer.data['image'][1:] +' -s 156 -ii 1 -o media/temp/'+ image_uuid +'.png')
        os.system('rembg i media/temp/'+ image_uuid +'.png media/result/'+ image_uuid +'.png')
        
        image = Image.open('media/result/' + image_uuid + '.png')
        article.image = 'result/' + image_uuid + '.png'
        article.save()

        return Response("스타일 제작 완료", status=status.HTTP_200_OK)