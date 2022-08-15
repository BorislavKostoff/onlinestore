from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product
from order.models import Order
from .serializers import ProductSerializer, OrderSerializer
from .pagination import CustomPagination


@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def orderStats(request):
    paginator = CustomPagination()
    paginator.page_size = 3
    orders = Order.objects.all()
    paginated_orders = paginator.paginate_queryset(orders, request)
    serilizer = OrderSerializer(paginated_orders, many=True)
    return paginator.get_paginated_response(serilizer.data)