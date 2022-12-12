from string import ascii_uppercase, ascii_lowercase, digits
from random import sample


def get_random_password(n) -> list:

    list_symbols = ascii_lowercase + ascii_uppercase + digits
    list_ = sample(list_symbols, n)
    return list_


print(get_random_password(8))
