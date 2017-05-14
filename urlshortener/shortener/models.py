from django.db import models
import random

# Create your models here.
def code_generator():
    a = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.sample(a*6,6))


class BigUrl(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,default="xyz",unique=True)
    last_modified= models.DateTimeField(auto_now=True)
    time_stamp= models.DateTimeField(auto_now_add=True)

    def save(self,*argv,**kwargs):
        print("something")
        self.shortcode = code_generator()
        super(BigUrl,self).save(*argv,**kwargs)

    def __str__(self):
        return str(self.url)
