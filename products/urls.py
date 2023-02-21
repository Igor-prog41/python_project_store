from django.urls import path
from .views import *

urlpatterns = [
# project path
    path('all/',ProductList.as_view()),

# test path
    path('category/list/',CategoryList.as_view()),
    path('list/',ProductList.as_view()),
    path('brand/list/',BrandList.as_view()),
    path('productreview/list/',ProductReviewList.as_view()),
    path('productcategory/list/',ProductCategoryList.as_view()),
    path('goods/',product_list),
    path('category/get/<int:pk>/',CategoryRetrieve.as_view()),
    path('good/<int:product_id>/',retrieve_product),
    path('good/delete/<int:product_id>/',delete_product),
    path('create/',CreateProduct.as_view()),
    path('update/<int:pk>/',ProductUpdate.as_view()),
    path('productreview/list/',ProductListWithReview.as_view()),
]

# /api/product/category/list/