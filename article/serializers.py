from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    class Meta:
        model = Article
        fields = ('id', 'image', 'likes_count',)