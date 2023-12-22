from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory


# Create your views here.

from .models import *           #imported models
from .forms import OrderForm    #created forms 

from .filters import OrderFilter


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    
    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()


    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'delivered':delivered, 'orders_pending':orders_pending}


    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})

def customers(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()

    total_orders = orders.count()

    myfilter = OrderFilter()

    context = {'customer': customer, 'orders':orders, 'total_orders':total_orders, 'myfilter':myfilter}
    return render(request, 'accounts/customers.html', context) 



def create_order(request, pk):

    order_form_set = inlineformset_factory(Customer, Order, fields= ('product', 'status'), extra = 10)
    customer = Customer.objects.get(id=pk)
    formset = order_form_set(queryset=Order.objects.none(),instance = customer)
    form = OrderForm(initial = {'customer':customer})

    if request.method == 'POST':
        formset = order_form_set(request.POST, instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset, }
    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):

    order = Order.objects.get(id = pk)

    form = OrderForm(instance = order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance= order)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        order.delete()    
        return redirect('/')
    context = {'order':order}
    return render(request, 'accounts/delete_order.html', context)
