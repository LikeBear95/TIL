# hw_7_2.py

class UserInfo():
    user_list = {}

    def get_user_info(self):
        try:
            self.name = input('이름을 입력하세요: ')
            self.age= int(input('나이를 입력하세요: '))
            self.user_list['name'] = self.name
            self.user_list['age'] = self.age
        except:
            print("나이는 숫자로 입력해야 합니다.")

    def display_user_info(self):
        if len(self.user_list) > 0:
            print('사용자 정보: ')
            print('이름:', self.user_list['name'])
            print(f'나이: {self.user_list["age"]}')
        else:
            print("사용자 정보가 입력되지 않았습니다.")

user1 = UserInfo()
user1.get_user_info()
user1.display_user_info()