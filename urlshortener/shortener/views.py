from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse , HttpResponseRedirect, Http404
# Create your views here.
from django.views import View
from .models import BigUrl
from .forms import SubmitUrlForm
from analytics.models import ClickEvent


def test_view(request):
    return HttpResponse("testing pass if you are viewing this page")


def fb_home_view(self,request, *args,**kwargs):
    if request.method==post:
        print(request.POST)
    return render(request, 'shortener/home.html',{})






class HomeView(View):
    def get(self, request,  *args,**kwargs):
        the_form = SubmitUrlForm()
        context = {
                "title": "enter your url",
                "form": the_form
                }
        return render(request, 'shortener/home.html',context)

    def post(self, request, *args , **kwargs):
        form = SubmitUrlForm(request.POST)
        context ={
            "title": "your entered url",
            "form": form
            }
        template = "shortener/home.html"
        if form.is_valid():
            print(form.cleaned_data.get("url"))
            new_url=form.cleaned_data.get("url")
            obj, created = BigUrl.objects.get_or_create(url=new_url)
            context = {
                    "object" : obj,
                    "created": created,
                    }
            if created:
                #  return render(request, 'shortener/success.html',new_context)
                template = "shortener/success.html"
            else:
                #  return render(request, 'shortener/already_exist.html',new_context)
                template = "shortener/already_exist.html"
                
        return render(request,template ,context)


#  def redirect_fb_view(request,shortcode=none, *args,**kwargs):
#      obj = get_object_or_404(bigurl, shortcode=shortcode)
#      return httpresponseredirect(obj.url)
#      #  return  httpresponse("hello {sc}".format(sc=obj.url))
#
#      try:
#          obj = bigurl.objects.get(shortcode = shortcode)
#      except:
#          obj  = bigurl.objects.all().first()
#      return httpresponse("hello {sc}".format(sc=obj))
#
#
#      obj_url = obj.url
#
#
#      obj_url = none
#      qs = bigurl.objects.filter(shortcode__iexact = shortcode.upper())
#      if qs.exists() and qs.count() ==1:
#          obj = qs.first()
#          obj_url = obj.url
#
#      #  obj = bigurl.objects.get(shortcode=shortcode)
#      return httpresponse("hello {sc}".format(sc=obj_url))
#
#
class URLRedirectView(View):
    def get(self, request,shortcode=None,  *args,**kwargs):
        #  print(shortcode)
        qs = BigUrl.objects.filter(shortcode__iexact=shortcode)
        if qs.count()!=1 and  not  qs.exists():
            raise Http404
        #  print(qs)
        #  obj = get_object_or_404(bigurl, shortcode__iexact=shortcode)
        #  #  return  httpresponse("hello again {sc}".format(sc=obj.url))
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
