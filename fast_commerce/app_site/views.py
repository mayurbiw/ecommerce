from django.shortcuts import render, HttpResponse
from .tasks import  sync_products
from rest_framework import viewsets, generics , views, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from app_site.models import Product, ReviseOrder
from  app_site.serializers import ProductSerializer, CustomUserSerializer, OrderSerializer, HistorySerilizer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from  fastsite import salesforce_models
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


    
class ProductViewSet(viewsets.ModelViewSet):
    #permission_classes = [AllowAny]
    """
    API endpoint that allows products to be viewed.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [IsAuthenticated]

class CustomUserCreate(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(views.APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    #permission_classes = [AllowAny]
    """
    API endpoint that allows orders to be viewed.
    """
    #username = request.user.username
    model = ReviseOrder
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        print(self.request.user.id)
        queryset = ReviseOrder.objects.filter(user_id=self.request.user.id)
        return queryset
    
    def create(self, request):
        for order in request.data:
            order["user_id"] = self.request.user.id
        serializer = OrderSerializer(data=request.data,many=True)
        if serializer.is_valid():
            order = serializer.save()
            if order:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerilizer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        print(self.request.user.id)
        queryset = ReviseOrder.objects.filter(user_id=self.request.user.id).select_related('Product2Id').values("Product2Id__name","Product2Id__UnitPrice","status")
        return queryset
 
     

    