from django.conf import settings
import random
import string

SHORTCODE_MIN = getattr( settings,"SHORTCODE_MIN" ,6)

def Code_generator(size =SHORTCODE_MIN ):
    a = string.ascii_letters + string.digits
    return "".join(random.sample(a*SHORTCODE_MIN,SHORTCODE_MIN))

def create_shortcode(instance,size=SHORTCODE_MIN):
    new_code= Code_generator(size= size )
    instance_class = instance.__class__
    query_set = instance_class.objects.filter(shortcode=new_code).exists()
    if query_set:
        return shortcode(size=size)
    return (new_code)

