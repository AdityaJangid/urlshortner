from django.db import models

# Create your models here.

class BigUrl(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,default="xyz",unique=True)
    last_modified= models.DateTimeField(auto_now=True)
    time_stamp= models.DateTimeField(auto_now_add=True)
    
    """ def save(self,*argv,**kwargs):
        print("something")
        self.shortcode = code_generator()
        super(BigUrl,self).save(*argv,**kwargs)
        """

    def __str__(self):
        return str(self.url)
