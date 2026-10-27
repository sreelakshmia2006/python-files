# class Animal:                                                    # single inheritance
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def bark(self):
#         print("Barking")

# d=Dog()
# d.eat()
# d.bark()



# class Camera:                                              # multiple inheritance
#     def photo(self):
#         print("Taking photo")
# class Phone:
#     def call(self):
#         print("Calling")
# class smartphone(Camera,Phone):
#     pass
# s=smartphone()
# s.photo()
# s.call()



# class Person:                                            # multilevel inheritance
#     def speak(self):
#         print("Speaking")
# class Student(Person):
#     def study(self):
#         print("Studying")
# class CollegeStudent(Student):
#     pass
# c=CollegeStudent()
# c.speak()
# c.study()



# class Animal:                                                  # hierarchial inheritance
#     def eat(self):
#         print("Eating")
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass

# d=Dog()
# c=Cat()
# d.eat()
# c.eat()



class Person:
    def work(self):
        print("Working")
class Student(Person):
    def study(Person):
        print("Studying")
class Employee(Person):
    def earn(self):
        print("Earning")

class Intern(Student, Employee):
    pass

i= Intern()
i.work()
i.study()
i.earn()