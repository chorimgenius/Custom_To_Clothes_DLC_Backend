from rest_framework import serializers
from article.models import Draft
from article.models import Style
from article.models import Article

class CustomStyleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'

class CustomViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Draft
        fields = '__all__'   
        
class ArticlePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ("id", "user", "draft", "style", "image")

class ArticleSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    class Meta:
        model = Article
        fields = ('id', 'image', 'likes_count',)

class ArticlePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("draft",)
