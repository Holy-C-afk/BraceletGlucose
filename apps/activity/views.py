from django.shortcuts import render
from django.http import HttpResponse

def activity_list(request):
    return HttpResponse("List of activities")

def activity_detail(request, pk):
    return HttpResponse(f"Details of activity {pk}")
