from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from product.servicess.engine import Engine
from django.db.models import Q

class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response({'data': serializer.data})

    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'detail': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)

class HelpMeToSearch(APIView):
    def get(self, request):
        keywords = request.GET.get('keyword', None)
        k_number = int(request.GET.get('k', 5))
        min_price = request.GET.get('min_price', None)
        max_price = request.GET.get('max_price', None)

        if keywords is None:
            return Response({'data': []})

        id_list = Engine.search_product(keywords, k_number)
        products = Product.objects.filter(id__in=id_list)

        # Apply price filters if provided
        if min_price is not None:
            products = products.filter(price__gte=float(min_price))
        if max_price is not None:
            products = products.filter(price__lte=float(max_price))

        serializer = ProductSerializer(products, many=True)
        return Response({'data': serializer.data})
    
class NormalSearch(APIView):
    def get(self , request):
        keywords = request.GET.get('keyword' , None)
        k_number = request.GET.get('k' , 0)
        min_price = request.GET.get('min_price' , None)
        max_price = request.GET.get('max_price' , None)

        filters = Q(title__icontains=keywords) | Q(category__icontains=keywords) | Q(brand__icontains=keywords)

        if min_price is not None:
            filters &= Q(price__gte=min_price)
        if max_price is not None:
            filters &= Q(price__lte=max_price)

        ps = Product.objects.filter(filters)[:k_number]

        serializer = ProductSerializer(ps , many=True)
        return Response({'data': serializer.data})
    