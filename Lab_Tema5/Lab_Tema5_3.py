import random
from string import ascii_letters, digits
import string

def get_random_password(n=8) -> str:
    field = ascii_letters + digits
    field2 = string.ascii_letters + string.digits
    random_str = random.sample(field, n)
    return random_str

print(get_random_password())
