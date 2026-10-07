# name = "Sreelakshmi"
# age = 21
# course = "Data Analytics"
# print(name)
# print(age)
# print(course)

# print(type(name))
# print(type(age))
# print(type(course))

# print("my name is", name)
# print("i am", age,"years old")
# print("i am studying", course)


# numbers = {10,10,20,30}                                                 
# numbers.add(40)
# print(numbers)

# numbers.remove(20)
# print(numbers)

# numbers.discard(30)
# print(numbers)

# a={1,2,3}
# b={3,4,5}
# print(a.union(b))
# print(a.intersection(b))

# numbers=(10,20,30,20)                                                  
# print(numbers.count(20))
# print(numbers.index(30))

# student = {1:{"name":"Sreelakshmi","age":21,"course":"Data analytics"},2:{"name":"nandha","age":18,"course":"science"}}  
# student[1]["name"]="aaaa"  
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student[3])
# print(student.get("name"))

# age = 21                                                               
# print(age.bit_length())

# price = 25.0                                                              
# print(price.is_integer())
# price = 25.5
# print(price.is_integer())



# name= int(input("enter your name : "))
# print(len(name))



number = int(input("Enter a number:"))
count = 0
while number > 0:
    number = number // 10
    count = count + 1
print("Length =", count)  




