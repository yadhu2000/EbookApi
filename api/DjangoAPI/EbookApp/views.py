from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EbookApp.models import Ebooks
from EbookApp.serializers import EbooksSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.filters import  SearchFilter, OrderingFilter


# Create your views here.

# class for authentication---------------------------

class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        emails = [user.email for user in User.objects.all()]
        return JsonResponse(emails, safe=False)


class authEbooks(APIView):
         authentication_classes = [authentication.TokenAuthentication]
         permission_classes = [permissions.IsAuthenticated]

        #  filter_backends = (SearchFilter, OrderingFilter)
        #  Search_fields = ('ID','Title','Author','Genre')

         def get(self, request,id=0, format=None):
            orderBy = self.request.query_params.get('orderBy')
            search = self.request.query_params.get('search')
            if (search ) :
                Ebook = Ebooks.objects.all().filter(Title=search)
            elif (orderBy):
                Ebook = Ebooks.objects.all().order_by(orderBy)
            else:
                Ebook = Ebooks.objects.all()
            
            Ebooks_serializer = EbooksSerializer(Ebook,many=True)
            return JsonResponse(Ebooks_serializer.data,safe=False)
         def post(self, request,id=0, format=None):
            Ebooks_data = JSONParser().parse(request)
            Ebooks_serializer = EbooksSerializer(data=Ebooks_data)
            if Ebooks_serializer.is_valid():
                Ebooks_serializer.save()
                return JsonResponse("Added Successfuly", safe=False)
            return JsonResponse("Failed to Add", safe=False)
         def put(self, request,_id=0, format=None):
            Ebooks_data = JSONParser().parse(request)
            Ebook = Ebooks.objects.get(ID=_id)
            Ebooks_serializer = EbooksSerializer(Ebook, data=Ebooks_data)
            if Ebooks_serializer.is_valid():
                Ebooks_serializer.save()
                return JsonResponse("Update Successfull", safe=False)
            return JsonResponse("Failed to update")
         def delete(self, request,_id=0, format=None):
            Ebook = Ebooks.objects.get(ID=_id)
            Ebook.delete()
            return JsonResponse("deleted Successfully", safe=False)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
# -----------------------------------------------------

# code for CRUD operations---------------------------------------


# @csrf_exempt

# def EbooksApi(request, _id=0, format=None):
#         if request.method == 'GET':
#             Ebook = Ebooks.objects.all()
#             Ebooks_serializer = EbooksSerializer(Ebook, many=True)
#             return JsonResponse(Ebooks_serializer.data, safe=False)
#         elif request.method == 'POST':
#             Ebooks_data = JSONParser().parse(request)
#             Ebooks_serializer = EbooksSerializer(data=Ebooks_data)
#             if Ebooks_serializer.is_valid():
#                 Ebooks_serializer.save()
#                 return JsonResponse("Added Successfuly", safe=False)
#             return JsonResponse("Failed to Add", safe=False)
#         elif request.method == "PUT":
#             Ebooks_data = JSONParser().parse(request)
#             Ebook = Ebooks.objects.get(ID=_id)
#             Ebooks_serializer = EbooksSerializer(Ebook, data=Ebooks_data)
#             if Ebooks_serializer.is_valid():
#                 Ebooks_serializer.save()
#                 return JsonResponse("Update Successfull", safe=False)
#             return JsonResponse("Failed to update")
#         elif request.method == 'DELETE':
#             Ebook = Ebooks.objects.get(ID=_id)
#             Ebook.delete()
#             return JsonResponse("deleted Successfully", safe=False)
