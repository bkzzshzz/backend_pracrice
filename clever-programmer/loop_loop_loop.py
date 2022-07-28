# sum of the numbers in a list

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [12, 34, 56, 76]


def sum_in_list(given_list):
    sum = 0
    for each_number in given_list:
        sum = sum + each_number
    return sum

print(sum_in_list(list_1))
print(sum_in_list(list_2))

# nice little tool called assert to check code
assert sum_in_list(list_1) == 45
assert sum_in_list(list_2) == 178