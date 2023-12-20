from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name="home"),
    path('products', views.products, name = 'products'),
    # path('customers', views.customers),
    path('customers/<str:pk>/', views.customers, name = 'customers'),
    path('create_order', views.create_order, name = 'create_order'),
    path('update_order/<str:pk>/', views.update_order, name = 'update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name = 'delete_order'),
]
