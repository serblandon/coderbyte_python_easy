class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello! My name is {self.name}")


person1 = Person("Alex")

person1.introduce()