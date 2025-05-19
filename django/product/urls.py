from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView , HelpMeToSearch , NormalSearch , LoadDB

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('help-me-to-serach' , HelpMeToSearch.as_view() , name="HelpMeToSearch"),
    path('normal-search' , NormalSearch.as_view()),
    path('load-db' , LoadDB.as_view() , name="LoadDB")
]
