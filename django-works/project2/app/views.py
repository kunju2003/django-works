from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sum(request,a,b):
  return HttpResponse(('sum='+str(a+b))+('<br>product='+str(a*b)))
