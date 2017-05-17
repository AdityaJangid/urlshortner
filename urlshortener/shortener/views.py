from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.views import View



def Redirect_FB_View(request,*args,**kwargs):
    return  HttpResponse("hello")



class Redirect_CB_View(View):
    def get(self, request, *args,**kwargs):
        return HttpResponse("hello again")
