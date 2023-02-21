from rest_framework import serializers
from .models import *


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"  


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandField(serializers.RelatedField):
    def to_representation(self, value):
        return {'id':value.id,"title":value.title}


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandField(many=False,read_only=True)
    reviews = ProductReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ('id','title','price','old_price','brand','quantity','reviews')   


class ProductListSerializer(serializers.ModelSerializer):
    brand = BrandField(many=False,read_only=True)
    class Meta:
        model = Product
        fields = ('id','title','price','old_price','brand','quantity') 


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"   

       



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"  