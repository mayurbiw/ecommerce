from django.urls import path
from . import views

from app_site.views import ProductViewSet, OrderViewSet, HistoryViewSet
from rest_framework import renderers


product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

Order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

history = HistoryViewSet.as_view({
     'get': 'list',
    'post': 'create'
}
)

product_detail = ProductViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    #path("", views.index, name="index"),
    path("register/",views.CustomUserCreate.as_view(), name="register"),
    path("products/",product_list,name='products'),
    path("history/",history,name='history'),
    path("orders/",Order_list,name='orders'),
    path('products/<pk>', product_detail, name='product-detail'),
    path('logout/blacklist/', views.BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
]
