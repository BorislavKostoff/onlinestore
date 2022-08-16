from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
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

class OrderAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPagination

    filterset_fields = ['date']

    def get_queryset(self):
        filter = {}
        queryset = Order.objects.all()

        date_start = self.request.GET.get('date_start', None)
        date_end = self.request.GET.get('date_end', None)
        metric = self.request.GET.get('metric', None)

        if date_start is not None:
            filter['date__gte'] = date_start

        if date_end is not None:
            filter['date__lte'] = date_end

        queryset = queryset.filter(**filter)

        return queryset