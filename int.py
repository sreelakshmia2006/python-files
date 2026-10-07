# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


n = 5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")

    for k in range(i+1):
        print("*",end = " ")

    print()



# l = [{"name":"sree","age":21,"phonenumber":9876543210},
#      {"name":"neha","age":23,"phonenumber":9876543211},
#      {"name":"diya","age":24,"phonenumber":9876543212}]
# phone=int(input("enter your phonenumber : "))
# for i in range(len(l)):
#     if l[i]["phonenumber"]==phone:
#         print(l[i])
#         break
#     else:
#         pass



# d={1:{"name":"sree","age":21,"phonenumber":9876543221},
#    2:{"name":"nandha","age":18,"phonenumber":9876543210},
#    3:{"name":"sidhu","age":23,"phonenumber":9876543211},
#    4:{"name":"rahul","age":22,"phonenumber":9876543212}}

# phone =int(input("enter your phonenumber :"))
# for i in d:
#     if d[i]["phonenumber"]==phone:
#         print(d[i])
#         break
#     else:
#         pass


# a=[["sree",21,9876543210],
#    ["sidharth",23,9876543211],
#    ["sandra",26,9876543212]]
# phone=int(input("enter your phonenumber:"))
# for i in a:
#    if i[2]==phone:
#     print(i)
#     break
# else:
#     pass



# l = [{"name":"sree","age":21,"phonenumber":9876543210},
#      {"name":"neha","age":23,"phonenumber":9876543211},
#      {"name":"diya","age":24,"phonenumber":9876543212}]
# phone=int(input("enter your phonenumber : "))
# for i in range(len(l)):
#     if l[i]["phonenumber"]==phone:
#         print(l[i])
#         break
# else:
#     print("not found")


# d={1:{"name":"sree","age":21,"phonenumber":9876543221},
#    2:{"name":"nandha","age":18,"phonenumber":9876543210},
#    3:{"name":"sidhu","age":23,"phonenumber":9876543211},
#    4:{"name":"rahul","age":22,"phonenumber":9876543212}}
# phone =int(input("enter your phonenumber :"))
# for i in d:
#     if d[i]["phonenumber"]==phone:
#         print(d[i])
#         break
# else:
#     print("not found")


# a=[["sree",21,9876543210],
#    ["sidharth",23,9876543211],
#    ["sandra",26,9876543212]]
# phone=int(input("enter your number:"))
# for i in a:
#    if i[2]==phone:
#       print(i)
#       break
# else:
#    print("not found")
    