# ws_3_3.py
import my_math
rental = dict()

def rental_book(name, number):
    my_math.decrease_book(number)
    rental = {'name': name, 'number': number}
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')
    return rental

rental_book('홍길동', 3)