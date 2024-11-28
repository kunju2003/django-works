from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sum(request,a,b):
  return HttpResponse('sum='+str(a+b))
def pro(requset,a,b):
  return HttpResponse('product='+str(a*b))