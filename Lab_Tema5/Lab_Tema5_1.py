import pprint
list_name = ['bin', 'dec', 'hex', 'oct']

def get_dict(list_name, val):
    dict_ = {}
    for name in list_name:
        if name != 'dec':
            dict_[name] = eval(name+f"({val})")
    else:
        dict_[name] = val
    return dict_

pprint.pprint([get_dict(list_name, val) for val in range(16)])

# TODO решить с помощью list comprehension и распечатать его