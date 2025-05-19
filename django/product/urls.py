from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView , HelpMeToSearch , NormalSearch

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('help-me-to-serach' , HelpMeToSearch.as_view() , name="HelpMeToSearch"),
    path('normal-search' , NormalSearch.as_view()),
]
