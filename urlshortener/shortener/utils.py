import random
import string

def Code_generator(size =6 ):
    a = string.ascii_letters + string.digits
    return "".join(random.sample(a*6,6))

def short_code(instance,size=6):
    new_code= Code_generator(size= size )
    instance_class = instance.__class__
    query_set = instance_class.objects.filter(shortcode=new_code).exists()
    if query_set:
        return shortcode(size=size)
    return (new_code)

