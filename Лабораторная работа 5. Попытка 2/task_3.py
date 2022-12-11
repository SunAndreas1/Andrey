from random import randint
def get_unique_list_numbers(start, finish, step) -> list[int]:

    start = -10
    finish = 10
    step = 15
    list_ = []
    while len(list_) != step:
        numb = randint(start, finish)
        if numb not in list_:
            list_.append(numb)
    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)

print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
