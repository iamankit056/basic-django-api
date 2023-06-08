from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        products_serialize = ProductSerializer(products, many=True)
        return Response(products_serialize.data, status=status.HTTP_200_OK)


    def post(self, request):
        product_serialize = ProductSerializer(data=request.data)

        if product_serialize.is_valid():
            product_serialize.save()
            return Response('created', status=status.HTTP_201_CREATED)
        return Response('not created', status=status.HTTP_406_NOT_ACCEPTABLE)
        

class ProductDetailView(APIView):
    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except:
            return None
        

    def get(self, request, product_id):
        product = self.get_product(product_id)

        if product is None:
            return Response('Product does not exist', status=status.HTTP_404_NOT_FOUND)

        products_serialize = ProductSerializer(product)
        return Response(products_serialize.data, status=status.HTTP_200_OK)
    

    def put(self, request, product_id):
        product = self.get_product(product_id)

        if product is None:
            return Response('Product does not exist', status=status.HTTP_404_NOT_FOUND)
        
        serialize_product = ProductSerializer(product, data=request.data)

        if serialize_product.is_valid():
            serialize_product.save()
            return Response('Product Updated Sucessesfully...', status=status.HTTP_205_RESET_CONTENT)
        
        return Response('Invalid Data', status=status.HTTP_406_NOT_ACCEPTABLE)


    def delete(self, request, product_id):
        product = self.get_product(product_id)
        
        if product is None:
            return Response('Product does not exist', status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response('deleted sucessesfully', status=status.HTTP_204_NO_CONTENT)

