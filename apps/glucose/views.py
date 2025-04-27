from django.shortcuts import render
from django.http import HttpResponse

def glucose_list(request):
    return HttpResponse("List of glucose readings")

def glucose_detail(request, pk):
    return HttpResponse(f"Details of glucose reading {pk}")
