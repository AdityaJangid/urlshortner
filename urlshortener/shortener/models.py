from django.db import models
from .utils import Code_generator

# Create your models here.

class BigUrl(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,unique=True, blank=True)
    last_modified= models.DateTimeField(auto_now=True)
    time_stamp= models.DateTimeField(auto_now_add=True)

    def save(self,*argv,**kwargs):
        if self.shortcode == "" or self.shortcode is None:
          self.shortcode = Code_generator()
        super(BigUrl,self).save(*argv,**kwargs)

    def __str__(self):
        return str(self.url)
