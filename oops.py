# class car:
#     def __init__(self,brand,colour):
#         self.brand=brand
#         self.colour=colour

#     def drive(self):
#         print(f"I love {self.colour} {self.brand} car so much")


# car1=car("Audi" , "Black")
# car2=car("Ciaz" , "Red")

# print(car1.brand)
# car2.drive()
# print(car2.colour)
# car1.drive()




class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def show_details(self):
        print(f"Name is {self.name}, Department is {self.department}, Salary is {self.salary}")
        print("Medical Checkup: Completed")

emp1=Employee("Anu" , "IT" , 50000)
emp2=Employee("Swetha" , "HR" , 40000)
emp3=Employee("Rahul" , "Sales" , 35000)
emp4=Employee("Riya" , "Finance" , 45000)

emp1.show_details()
emp2.show_details()
emp3.show_details()
emp4.show_details()

