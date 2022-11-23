from rest_framework import serializers
from article.models import Article
from article.models import Draft

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        
class CustomViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Draft
        fields = '__all__'