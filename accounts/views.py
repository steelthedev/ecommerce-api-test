from django.shortcuts import render
from .serializers import ProfileSerializer, RegisterSerializer
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication,permissions



class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        if request.method =="POST":
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                account = serializer.save()
                account.save()
                return Response(serializer.data)
            return HttpResponse(status.HTTP_400_BAD_REQUEST)
        return HttpResponse(status.HTTP_400_BAD_REQUEST)


class ProfileListView(APIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get_object(self):
        try:
           return Profile.objects.all()
        except ObjectDoesNotExist:
            return Http404
    def get(self,request):
        profile = self.get_object()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

class GetProfile(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        try:
            profile = request.user
        except ObjectDoesNotExist:
            return Http404
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)


class EditProfile(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def patch(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

