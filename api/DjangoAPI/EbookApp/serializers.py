from rest_framework import serializers
from EbookApp.models import Ebooks

from django.contrib.auth.models import User

#seializer class for user---------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']
#-----------------------------------------------------


#seializer class for Ebooks--------------------------

class EbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ebooks
        fields=('ID','Title','Author','Genre','Review','Favorite')

#-----------------------------------------------------