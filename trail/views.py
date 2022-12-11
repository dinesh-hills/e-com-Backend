from django.shortcuts import render
from django.db.models.aggregates import Count
from django.http import HttpResponse
# from .models import Product, OrderItem, Order, Customer

# def view_test(request):
    
#     result = Order.objects.aggregate(count=Count('id'))
#     data = {
#         'response_code': HttpResponse(request),
#         'result': result
#     }    
#     return render(request, 'index.html', data)