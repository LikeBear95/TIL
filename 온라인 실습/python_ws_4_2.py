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
    dummy_data.append(parsed_data['name'])

# 데이터 리스트 출력
print(dummy_data)