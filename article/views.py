from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from article.models import Draft
from article.serializers import CustomViewSerializer

class CustomView(APIView):
    def get(self,request):
        draft = Draft.objects.all()
        serializer = CustomViewSerializer(draft, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)