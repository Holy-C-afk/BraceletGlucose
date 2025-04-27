from django.shortcuts import render
from django.http import HttpResponse

def insulin_list(request):
    return HttpResponse("List of insulin doses")

def insulin_detail(request, pk):
    return HttpResponse(f"Details of insulin dose {pk}")
