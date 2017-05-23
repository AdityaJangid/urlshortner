from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
from django.views import View
from .models import BigUrl


def test_view(request):
    return HttpResponse("testing pass if you are viewing this page")


def fb_home_view(self,request, *args,**kwargs):
    if request.method==post:
        print(request.POST)
    return render(request, 'shortener/home.html',{})






class HomeView(View):
    def get(self, request,  *args,**kwargs):
        return render(request, 'shortener/home.html',{})

    def post(self, request, *args , **kwargs):
        #  some_dict = {} some_dict.get('url', "http://www.canis.com")
        #  print(request.POST)
        print(request.POST["url"])
        print(request.POST.get("url"))
        return render(request, 'shortener/home.html',{})


#  def Redirect_FB_View(request,shortcode=None, *args,**kwargs):
#      obj = get_object_or_404(BigUrl, shortcode=shortcode)
#      return HttpResponseRedirect(obj.url)
#      #  return  HttpResponse("hello {sc}".format(sc=obj.url))
#
#      try:
#          obj = BigUrl.objects.get(shortcode = shortcode)
#      except:
#          obj  = BigUrl.objects.all().first()
#      return HttpResponse("hello {sc}".format(sc=obj))
#
#
#      obj_url = obj.url
#
#
#      obj_url = None
#      qs = BigUrl.objects.filter(shortcode__iexact = shortcode.upper())
#      if qs.exists() and qs.count() ==1:
#          obj = qs.first()
#          obj_url = obj.url
#
#      #  obj = BigUrl.objects.get(shortcode=shortcode)
#      return HttpResponse("hello {sc}".format(sc=obj_url))
#
#
class Redirect_CB_View(View):
    def get(self, request,shortcode=None,  *args,**kwargs):
        obj = get_object_or_404(BigUrl, shortcode=shortcode)
        #  return  HttpResponse("hello again {sc}".format(sc=obj.url))
        return HttpResponseRedirect(obj.url)


