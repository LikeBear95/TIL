# main.py

# 아래 함수를 수정하시오.
def find_min_max(numbers):
    # return min(numbers), max(numbers)
    min_value = numbers[0]
    max_value = numbers[0]

    for number in numbers:
        if min_value > number:
            min_value = number

        if max_value < number:
            max_value = number

    return min_value, max_value

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
