from django.db import models
from .utils import Code_generator
from .utils import create_shortcode

# Create your models here.
class BigUrlManager(models.Manager):
    # gives all the unactive urls

    def unactive(self, *args, **kwargs):
        query_set = super(BigUrlManager, self).all(*args, **kwargs)
        query_set = query_set.filter(Active = False)
        return query_set


    #gives all the  active urls

    def active(self, *args, **kwargs):
        query_set = super(BigUrlManager, self).all(*args, **kwargs)
        query_set = query_set.filter(Active = True)
        return query_set
    

    #change all the shortcodes all at  once

    def refresh_shortcodes(self, items = None):
        print(items)
        new_codes = 0
        qs = BigUrl.objects.filter(id__gte=1) 
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q)
            print(q.shortcode)
            #  print(q.objects.filter(id=q))
            q.save()
            new_codes = new_codes+1
        return "New codes made: {i}".format(i=new_codes)

class BigUrl(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,unique=True, blank=True)
    last_modified= models.DateTimeField(auto_now=True)
    time_stamp= models.DateTimeField(auto_now_add=True)
    Active = models.BooleanField(default = True)
    objects = BigUrlManager()
    

    def save(self,*argv,**kwargs):
        if self.shortcode == "" or self.shortcode is None:
          self.shortcode = create_shortcode(self)
        super(BigUrl,self).save(*argv,**kwargs)

    def __str__(self):
        return str(self.url)
