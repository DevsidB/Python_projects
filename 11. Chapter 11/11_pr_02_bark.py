class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        return "Bhow Bhow"
sound= Dog()
print(sound.bark())