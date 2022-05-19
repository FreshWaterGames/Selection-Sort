import random


def random_list(length):
    l = [random.randint(-50, 9999) for i in range(length)]
    return l


def selection_sort(target_list):
    for start_i in range(len(target_list)):  # gets list lenght
        lowest_i = start_i  # assumes that lowest value is starting value

        # finds smallest value that occurs after start_i
        for check_i in range(start_i + 1, len(target_list)):  # +1 to start at value after starting value
            if target_list[check_i] < target_list[lowest_i]:  # if value found is lower than lowest_i
                lowest_i = check_i  # lowest_1 index = check_i index

        # swaps lowest value and start value
        target_list[start_i], target_list[lowest_i] = target_list[lowest_i], target_list[start_i]

    return target_list


def selection_sort_fast(target_list):
    for start_i in range(len(target_list)):  # gets list lenght
        check_list = target_list[start_i:]  # (colon = list slicing based off index) offloads processing to C code of python
        lowest_i = check_list.index(min(check_list)) + start_i  # adds start_list to account for list splicing

        # swaps lowest value and start value
        target_list[start_i], target_list[lowest_i] = target_list[lowest_i], target_list[start_i]
    return target_list


x = random_list(3000)
print(x)
print(selection_sort_fast(x))
