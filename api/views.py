from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer,OrderSerializer,ProudctInfoSerializer
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.views import APIView

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
     
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()




class ProductCreateAPIView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    def create(self,request,*args,**kwargs):
        print(request.data)
        return super().create(request,*args,**kwargs)
    

class ProductDetailAPIVew(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class ProductInfoAPIView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProudctInfoSerializer({
        'product' : products,
        'count' : len(products),
        'max_price' : products.aggregate(max_prize=Max('price'))['max_prize']

        })
        return Response(serializer.data)

