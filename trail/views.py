from django.shortcuts import render
from django.http import HttpResponse

def view_test(request):
    return render(request, 'index.html', {'response_code': HttpResponse(request)})