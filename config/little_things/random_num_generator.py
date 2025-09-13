import random

from urllib3.util.util import reraise


def get_random_num(lst=None, of=None, to=None):
    if lst:
        lst = list(lst.split(sep=' '))
        result = random.choice(lst)
        return result
    else:
        result = random.randrange(of, to)
        return result