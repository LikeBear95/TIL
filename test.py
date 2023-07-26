# hw_6_4.py


# 아래 함수를 수정하시오.
def add_item_to_dict(dict, key, value):
    dict.update(key = value)
    return dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)


# person = {'name': 'Alice', 'age': 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}

# person.update(other_person)
# print(person)

# person.update(age=50)
# print(person)

# person.update(country='KOREA')
# print(person)