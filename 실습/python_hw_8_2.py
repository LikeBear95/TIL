# hw_8_2.py

# 아래 함수를 수정하시오.
def check_number():
    try:
        # 사용자로부터 숫자를 입력
        user_input = float(input('숫자를 입력하세요: '))

        if user_input > 0:
            print("양수입니다.")
        elif user_input == 0:
            print("0입니다.")
        elif user_input < 0:
            print("음수입니다.")

    # 숫자가 아닐 경우 실행
    except ValueError:
        print("잘못된 입력입니다.")

check_number()
