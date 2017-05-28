from django.db import models

# Create your models here.
from shortener.models import BigUrl


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance( instance, BigUrl):
            obj, created = self.get_or_create(big_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None




class ClickEvent(models.Model):
    big_url = models.OneToOneField(BigUrl)
    count = models.IntegerField(default=0)
    last_modified= models.DateTimeField(auto_now=True)
    time_stamp= models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()


    def __str__(self):
        return "{i}".format(i=self.count)
