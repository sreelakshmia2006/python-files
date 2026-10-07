# class Student :                                             # constructors
#     def __init__(self,name):
#         self.name = name
# s = Student("Anu")
# print(s.name)



# class Student :                                             # default constructor
#     def __init__(self):
#         print("Student created")
# s = Student()



# class Student :                                             # parameterized constructor
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s = Student("Anu",21)
# print(s.name)
# print(s.age)



# class parent :                                              # super()
#     def show(self):
#         print("parent")
# class child(parent):
#     def display(self):
#         pass
# c=child()
# c.show()



# class Parent :                                              # super() with constructor
#     def __init__(self):
#         print("Parent constructor")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")
# c = Child()



# from abc import ABC, abstractmethod                             # data abstraction
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# d = Dog()
# d.sound()


from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass

class BMW(Car):
    def start(self):
        print("Car started")

c = BMW()
c.start()