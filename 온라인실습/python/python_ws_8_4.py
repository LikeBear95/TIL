# ws_8_4.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0 

class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

    def bark(self):
        print('멍멍!')

class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

    def meow(self):
        print('야옹!')

class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound

    def access_num_of_animal(self):
        return Animal.num_of_animal

    def make_sound(self):
        print(f'{self.sound}')

    def play(self):
        print('애완동물과 놀기')

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()