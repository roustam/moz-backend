from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import TileProduct,MessageModel,TileColors, TileUsage,TileSurface
from products.api.serializers import ProductsSerializer,TileRecordSerializer,CaptchaSerializer,PropertiesSerializer
from rest_framework import generics
import django_filters.rest_framework as filters
from url_filter.integrations.drf import DjangoFilterBackend
from django.http import QueryDict
from url_filter.filtersets import ModelFilterSet
from django.http import HttpResponse
from django.template import loader
from collections import namedtuple


def index(request):
    template = loader.get_template('customerform.html')
    context = {}
    return HttpResponse(template.render(context, request))

class RecPropertyView(viewsets.ViewSet):
    props_tuple = namedtuple('record_properties', ('colors', 'surfaces', 'usages'))
    def list(self, request):
        object_props = self.props_tuple(
            colors = TileColors.objects.all(),
            surfaces = TileSurface.objects.all(),
            usages = TileUsage.objects.all(),
        )
        serializer = PropertiesSerializer(object_props)
        return Response(serializer.data)


class TilePageView(APIView):
    def get(self,request,pk):
        tile_rec = TileProduct.objects.get(pk=pk) #get rec from db
        serializer = TileRecordSerializer(tile_rec) # made a json from it
        return Response(serializer.data) # returned to sender

class ProductsFilterView(generics.ListAPIView):
    queryset = TileProduct.objects.filter(tile_is_active=True)
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['tile_name', 'price', 'tile_color','tile_usage','tile_surface','color_qty' ]

class ProductListView(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
         queryset = TileProduct.objects.filter(tile_is_active=True)
         tile_rec = self.request.query_params.get('tile_name', None)
         return queryset

class MessageView(APIView):

    def get(self, request, format=None):
        snippets = MessageModel.objects.all()
        serializer = CaptchaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CaptchaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
