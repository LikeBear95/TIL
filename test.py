<<<<<<< HEAD
k = 5
lst = []
for i in range(-1, k):
    lst.append(i)

print(lst)
=======
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	numbers = input()
	number_list = list(map(int, numbers.split(" ")))
	result = 0
	for i in number_list:
         if i % 2 != 0:
            result += int(i)

print(result)
>>>>>>> a0c15f2894e4edb4bd5f67a7ef7b09d396eb745a
