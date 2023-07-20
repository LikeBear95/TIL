# 실습 번호.py
number_of_people = 0
from book import decrease_book as db

def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    return {'name': name, 'age': age, 'address': address}

user_list = map(create_user, name, age, address)
many_user = list(user_list)

info_dict = lambda user: {'name': user['name'], 'age': user['age']}
info_list = map(info_dict, many_user)
info = list(info_list)

def rental_book(dic):
    rentbook = dic['age'] // 10
    db(rentbook)
    print(f"{dic['name']}님이 {dic['age']}권의 책을 대여하였습니다.")

for i in range(len(info)):
    rental_book(info[i])