import random
import string

def Code_generator():
    a = string.ascii_letters + string.digits
    return "".join(random.sample(a*6,6))

