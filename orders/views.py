
from .models import Order
from .serializers import MyOrderSerializer, OrderSerializer
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication,permissions




class CreateOrder(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getUserOrder(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,user):
        try:
            return Order.objects.filter(user=user)
        except ObjectDoesNotExist:
            return Http404
    def get(self,request):
        order = self.get_object(request.user)
        serializer = MyOrderSerializer(order, many=True)
        return Response(serializer.data)
