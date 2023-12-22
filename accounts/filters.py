import django_filters 
from .models import * 

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fileds = '__all__'
    Meta.fields = '__all__'