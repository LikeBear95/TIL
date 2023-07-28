# main.py

# 아래 함수를 수정하시오.
def count_character(string, char):
    # return string.count(char)
    count = 0
    for s in string:
        if s == char:
            count += 1
    return count
    

result = count_character("Hello, World!", "o")
print(result) # 2
