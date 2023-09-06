# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        # 이름과 나이를 입력
        try:
            user_name = input('이름을 입력하세요: ')
            user_age = int(input('나이를 입력하세요: '))
            self.user_data['name'] = user_name
            self.user_data['age'] = user_age
        # 잘못된 형식을 입력할 경우
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        # 유저 데이터를 입력 받았는지 확인
        if len(self.user_data) > 0:
            print('사용자 정보: ')
            print(f'이름: {self.user_data["name"]}')
            print(f'나이: {self.user_data["age"]}')
        # 유저 데이터가 없다면 오류문구 출력
        else:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()
