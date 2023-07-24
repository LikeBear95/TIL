# ws_8_2.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0 

class Dog(Animal):
    def __init__(self, bark):
        self._bark = bark
        Animal.num_of_animal += 1

    def bark(self):
        print(f'{self._bark}!')

class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

class Pet(Dog, Cat):
   def access_num_of_animal():
       return Animal.num_of_animal

dog1 = Dog("멍멍")
dog1.bark()
