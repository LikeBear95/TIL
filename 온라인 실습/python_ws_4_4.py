import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    # 특정 데이터 리스트에 저장
    if float(((parsed_data['address'])['geo'])['lat']) > -80.0 and float(((parsed_data['address'])['geo'])['lat']) < 80.0:
            if float(((parsed_data['address'])['geo'])['lng']) > -80.0 and float(((parsed_data['address'])['geo'])['lng']) < 80.0:
                dummy_data.append({'company': (parsed_data['company'])['name'], 'lat':((parsed_data['address'])['geo'])['lat'], 'lng': ((parsed_data['address'])['geo'])['lng'], 'name': parsed_data['name']})

# 데이터 리스트 출력
# print(dummy_data)

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

def create_user(data):
    censored_user_list = []
    for i in range(len(data)):
        user_dict = {data[i]['company']: [data[i]['name']]}
        test = censorship(user_dict)
        if test == True:
            censored_user_list.append(user_dict)
    print(censored_user_list)
    return censored_user_list

def censorship(dict):
    for i in range(len(black_list)):
        if black_list[i] == (list(dict.keys())[0]):
            print(f"{black_list[i]}소속의 {dict[black_list[i]]}은/는 등록할 수 없습니다.")
            return False
        else:
            if i+1 == len(black_list):
                print("이상 없습니다.")
                return True
            else:
                continue

create_user(dummy_data)