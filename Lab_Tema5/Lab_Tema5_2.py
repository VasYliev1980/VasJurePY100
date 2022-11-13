import random

def get_unique_list_nuuumbers() -> list[int]:
    a = []
    while len(a) < 15:
        val = random.randint(0, 14)
        if val not in a:
            a.append(val)
    return a

print(get_unique_list_nuuumbers)
