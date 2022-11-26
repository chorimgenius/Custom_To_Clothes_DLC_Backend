from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from article.models import Article
from user.serializers import UserSerializer, CustomObtainPairSerializer, ProfileSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer
    
class ProfileView(APIView):
    def get(self, request):
        article = Article.objects.filter(user=request.user)
        print(article)
        serializer = ProfileSerializer(article, many=True)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)