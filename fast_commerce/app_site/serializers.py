from django.contrib.auth.models import User, Group
from app_site.models import Product, ReviseOrder
from rest_framework import serializers
from  fastsite import salesforce_models


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        )
    
    class Meta:
        model = Product
        fields = ['url','id','name', 'product_code', 'description','family','UnitPrice']


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviseOrder
        list_serializer_class = serializers.ListSerializer
        fields = ('Product2Id', 'user_id','status',)

class HistorySerilizer(serializers.Serializer):
    Product2Id__name = serializers.CharField(max_length=200,required=True)
    Product2Id__UnitPrice = serializers.CharField(max_length=200,required=True)
    status = serializers.CharField(max_length=200)

