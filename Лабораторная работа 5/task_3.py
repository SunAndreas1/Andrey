def get_unique_list_numbers(start, finish, step) -> list[int]:
    from random import sample
    list_ = sample(range(start, finish + 1), step)
    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)


print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
