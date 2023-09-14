from random import randint

def fill_array_with_random_numbers(size):
    return [randint(1, 9) for _ in range(size)]

def add_arrays_with_carry(first_array, second_array):
    max_size = max(len(first_array), len(second_array))
    result_array = []
    temp = 0

    for i in range(max_size):
        first_digit = first_array[-i - 1] if i < len(first_array) else 0
        second_digit = second_array[-i - 1] if i < len(second_array) else 0
        total = first_digit + second_digit + temp
        temp = total // 10
        result_array.insert(0, total % 10)
    while len(first_array) < len(second_array):
        first_array.insert(0, 0)
    while len(second_array) < len(first_array):
        second_array.insert(0, 0)
    if temp > 0:
        result_array.insert(0, temp)

    return result_array

first_arr_size = int(input("Enter size of 1 arr: "))
second_arr_size = int(input("Enter size of 2 arr: "))

first_array = fill_array_with_random_numbers(first_arr_size)
second_array = fill_array_with_random_numbers(second_arr_size)

result_array = add_arrays_with_carry(first_array, second_array)

print(f"First array: {first_array}")
print(f"Second array: {second_array}")
print(f"Result: {result_array}")
