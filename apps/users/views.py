from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    return HttpResponse("List of users")

def user_detail(request, pk):
    return HttpResponse(f"Details of user {pk}")