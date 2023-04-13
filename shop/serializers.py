from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",'username','password','first_name','last_name','email')
        extra_kwargs = {'password':{'write_only':True,'required':True}}


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ['prouser']

    def validate(self,attrs):
        attrs['prouser'] = self.context['request'].user
        return attrs
    
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['prouser'] = UserSerializer(instance.prouser).data
        return response