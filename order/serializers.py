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
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('image',) 
        
class CartViewSerializer(serializers.ModelSerializer):
    article_user = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    article = ArticleSerializer()
    
    def get_article_user(self, obj):    
        return obj.user.username
    
    def get_price(self, obj):
        return obj.size.price
    
    def get_size(self, obj):
        return obj.size.size
    
    class Meta:
        model = Order
        fields = ('article_user','id','mount','size','article','user','price',)

class OrderListViewSerializer(serializers.ModelSerializer):
    article_user = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    article = ArticleSerializer()
    
    def get_article_user(self, obj):    
        return obj.user.username
    
    def get_price(self, obj):
        return obj.size.price
    
    def get_size(self, obj):
        return obj.size.size
    
    class Meta:
        model = Order
        fields = ('article_user','id','mount','size','status','article','user','price',)
