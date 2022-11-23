from rest_framework import serializers
from order.models import Order
from article.models import Article


class OrderViewSerializer(serializers.ModelSerializer):
    article_user = serializers.SerializerMethodField()

    def get_article_user(self, obj):    
        return obj.user.username
    
    class Meta:
        model = Article
        fields = ('id', 'article_user', 'image', 'user', 'draft',)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('mount', 'status',)

