# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(numbers):
    result = []
    while numbers:
        number = numbers.pop(0)
        if number % 2 == 0:
            result.extend([number])
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
