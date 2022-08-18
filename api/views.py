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

        result = {}
        months = [0,0,0,0,0,0,0,0,0,0,0,0]
        jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = months

        if date_start is not None:
            filter['date__gte'] = date_start

        if date_end is not None:
            filter['date__lte'] = date_end

        queryset = queryset.filter(**filter)

        # orders = queryset

        # if metric == 'count':
            #for order in orders['results']:
            #    if "2022-01" in order['date']:
            #        jan += len(order['products'])
            #        result['2022 JAN'] = jan
            #    if "2022-02" in order['date']:
            #        feb += len(order['products'])
            #        result['2022 FEB'] = feb
            #    if "2022-03" in order['date']:
            #        mar += len(order['products'])
            #        result['2022 MAR'] = mar
            #    if "2022-04" in order['date']:
            #        apr += len(order['products'])
            #        result['2022 APR'] = apr
            #    if "2022-05" in order['date']:
            #        may += len(order['products'])
            #        result['2022 MAY'] = may
            #    if "2022-06" in order['date']:
            #        jun += len(order['products'])
            #        result['2022 JUN'] = jun
            #    if "2022-07" in order['date']:
            #        jul += len(order['products'])
            #        result['2022 JUL'] = jul
            #    if "2022-08" in order['date']:
            #        aug += len(order['products'])
            #        result['2022 AUG'] = aug
            #    if "2022-09" in order['date']:
            #        sep += len(order['products'])
            #        result['2022 SEP'] = sep
            #    if "2022-10" in order['date']:
            #        oct += len(order['products'])
            #        result['2022 OCT'] = oct
            #    if "2022-11" in order['date']:
            #        nov += len(order['products'])
            #        result['2022 NOV'] = nov
            #    if "2022-12" in order['date']:
            #        dec += len(order['products'])
            #        result['2022 DEC'] = dec
            #return result



        return queryset