# def course(name,course_name="data analytics"):
#     print(name,course_name)

# name = "sreelakshmi"
# course_name = "python"
# course(name,course_name)


# def total_marks(*args):
#     return sum(args)


# answer = total_marks(45,50,60,75,80)
# print(answer)



# def details(**a):
#     for key,value in a.items():
#         print(key,value)

# details(name="sreelakshmi",age=21,course="data analytics")

# x=10
# def test():
    
#     print(x)

# test()
# print(x)



# count=0
# def increase():
#     # global count
#     # count+=1
#     pass
# increase()
# print(count)



litre = float(input("enter the amount of water used:"))
if litre <= 100:
    amount = litre*5
elif litre <= 200:
    amount = (100*5)+((litre-100)*10)
else:
    amount = (100*5)+(100*10)+((litre-200)*20)
print("Litres used:", litre)
print("Total amount:", amount)










