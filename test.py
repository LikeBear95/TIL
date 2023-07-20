list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

# is_book = True

# for i in range(len(rental_book)):
#     for j in range(len(list_of_book)):
#         if rental_book[i] == list_of_book[j]:
#             break
#         else:
#             if j + 1 == len(list_of_book):
#                 is_book = False
#                 print(f'{rental_book[i]} 은/는 보유하고 있지 않습니다.')
#                 break
#     if is_book == False:
#         break
#     else:
#         if i + 1 == len(rental_book):
#             print("모든 도서가 대여 가능한 상태입니다.")

# missing_book = [ if j != ]

missing_book = set(rental_book) - set([ rental_book[i] for i in range(len(rental_book)) for j in range(len(list_of_book)) if rental_book[i] == list_of_book[j] ])
print(missing_book)

if len(missing_book) == 0:
    print("모든 도서가 대여 가능한 상태입니다.")
else:
    for i in range(len(missing_book)):
        print(f'{list(missing_book)[i]} 을/를 보충하여야 합니다.')
