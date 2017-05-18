from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
# Create your views here.
from django.views import View
from .models import BigUrl



def Redirect_FB_View(request,shortcode = None, *args,**kwargs):
    #  try:
    #      obj = BigUrl.objects.get(shortcode = shortcode)
    #  except:
    #      obj  = BigUrl.objects.all().first()



    obj_url = None
    qs = BigUrl.objects.filter(shortcode__iexact = shortcode.upper())
    if qs.exists() and qs.count() ==1:
        obj = qs.first()
        obj_url = obj.url
    return  HttpResponse("hello {sc}".format(sc=obj__url))



class Redirect_CB_View(View):
    def get(self, request,shortcode=None,  *args,**kwargs):
        obj = BigUrl.objects.get(shortcode=shortcode)
        return  HttpResponse("hello again {sc}".format(sc=obj.url))
