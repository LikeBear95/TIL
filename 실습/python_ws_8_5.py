# ws_8_5.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0 

class Dog(Animal):
    sound = '멍멍'
    def __init__(self):
        Animal.num_of_animal += 1

    # def bark(self):
    #     print(f'{self.sound}!')

class Cat(Animal):
    sound = '야옹'
    def __init__(self):
        Animal.num_of_animal += 1

    # def meow(self):
    #     print(f'{self.sound}!')

class Pet(Dog, Cat):
    # def __init__(self, sound):
    #     self.sound = super().sound

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다'


    # def access_num_of_animal(self):
    #     return Animal.num_of_animal

    # def make_sound(self):
    #     print(f'{self.sound}')

    # def play(self):
    #     print('애완동물과 놀기')

# pet1 = Dog()
# pet2 = Cat()
pet3 = Pet()
# print(pet1.sound)
# print(pet2.sound)
print(pet3)