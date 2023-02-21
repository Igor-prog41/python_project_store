from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import * 
import json


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.filter(is_active=True) 


class ProductList(generics.ListAPIView):
    #serializer_class = ProductSerializer
    serializer_class = ProductListSerializer   #serializer without discription
    queryset = Product.objects.all()


class ProductListWithReview(generics.ListAPIView):
    serializer_class = ProductSerializer   
    queryset = Product.objects.all()


class BrandList(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class ProductReviewList(generics.ListAPIView):
    serializer_class = ProductReviewSerializer
    queryset = ProductReview.objects.all()


class ProductCategoryList(generics.ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class CategoryRetrieve(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductUpdate(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


def product_list(request):
    products = Product.objects.all()
    prods_ls = []
    for prod in products:
        tmp_prod = {
            "id": prod.id,
            "title": prod.title,
            "price": float(prod.price),
            "old_price": float(prod.price),
            "quantity": prod.quantity,
            "brand_id": str(prod.brand), 
        }
        prods_ls.append(tmp_prod)
    return HttpResponse(json.dumps(prods_ls))


def retrieve_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            "id":product.id,
            "title":product.title,
            "price":float(product.price),
            "old_price":float(product.price),
            "quantity":product.quantity,
            "brand":str(product.brand),
        }
    except Product.DoesNotExist:
        data = {"error" : "not such product"}
    return HttpResponse(json.dumps(data))


def delete_product(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            "id":product.id,
            "massage":"delete success",
        }
        product.delete()
    except Product.DoesNotExist:
        data = {
            "error":"product does not exist"
        }
    return HttpResponse(json.dumps(data))
