from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views



urlpatterns = [
    path('', views.SellerViewSet.as_view(), name ='seller-list'),
    path('<int:pk>/', views.SellerDetailViewSet.as_view(), name="seller-detail"),
    # path('<int:pk>/', views.ProdutoDetailViewSet.as_view(), name="produto-detail"),
    path('products/', views.ProdutoViewSet.as_view(),name='product-list')
]