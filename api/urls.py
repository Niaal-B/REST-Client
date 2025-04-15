from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.ProductListCreateAPIView.as_view()),
    path('product/info/',views.ProductInfoAPIView.as_view()),
    path('product/<int:pk>/',views.ProductDetailAPIVew.as_view()),
    path('orders/',views.OrderListAPIView.as_view()),
    path('user-orders/',views.UserOrderListAPIView.as_view()),

]
