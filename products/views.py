from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

# Create your views here.

from .models import Product
from .serializers import ProductSerializer

class ProdustListView(
    APIView, UpdateModelMixin, DestroyModelMixin
):
    def get(self, request, id=None):
        if id:
            try :
                query = Product.objects.get(id=id)
            except Product.DoesNotExist:
                return Response({'errors' : 'This Product does not exists'}, status=400)
            
            read_seralizer = ProductSerializer(query)
        else:
            query = Product.objects.all()
            read_seralizer = ProductSerializer(query, many=True)
        return Response(read_seralizer.data)

def post(self, request):
    create_serializer = ProductSerializer(data=request.data)
    if create_serializer.is_valid():
         product_item_object = create_serializer.save()
         read_serializer = ProductSerializer(product_item_object)
         return Response(read_serializer.data, status=201)
    return Response(create_serializer.errors, status=400)

def put(self, request, id=None):
    try:
        product_item = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'errors' : 'This product does not exits'}, status=400)

    update_serializer = ProductSerializer(product_item, data=request.data)
    
    if update_serializer.is_valid:
        product_item_object = update_serializer.save()
        read_serializer = ProductSerializer(product_item_object)
        return Response(read_serializer.data, status=200)
    return Response(update_serializer.errors, status=400)


def delete(self, request, id=None):
    try:
        product_item = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'errors' : 'This product does not exits'}, status=400)
    product_item.delete()
    return Response(status=204)