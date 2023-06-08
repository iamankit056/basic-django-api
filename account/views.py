from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serialize = UserSerializer(users, many=True)
        return Response(users_serialize.data, status=status.HTTP_200_OK)


    def post(self, request):
        user_serialize = UserSerializer(data=request.data)

        if user_serialize.is_valid():
            user_serialize.save()
            return Response('created', status=status.HTTP_201_CREATED)
        return Response('not created', status=status.HTTP_406_NOT_ACCEPTABLE)
        

class UserDetailView(APIView):
    def get_product(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return None
        

    def get(self, request, user_id):
        user = self.get_product(user_id)

        if user is None:
            return Response('Product does not exist', status=status.HTTP_404_NOT_FOUND)

        user_serialize = UserSerializer(user)
        return Response(user_serialize.data, status=status.HTTP_200_OK)
    

    def put(self, request, user_id):
        user = self.get_product(user_id)

        if user is None:
            return Response('Product does not exist', status=status.HTTP_404_NOT_FOUND)
        
        serialize_user = UserSerializer(user, data=request.data)

        if serialize_user.is_valid():
            serialize_user.save()
            return Response('Product Updated Sucessesfully...', status=status.HTTP_205_RESET_CONTENT)
        
        return Response('Invalid Data', status=status.HTTP_406_NOT_ACCEPTABLE)


    def delete(self, request, user_id):
        user = self.get_product(user_id)
        
        if user is None:
            return Response('Product does not exist', status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response('deleted sucessesfully', status=status.HTTP_204_NO_CONTENT)

