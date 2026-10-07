# for i in range(1,11):
#     print(i)

# for i in range(1,50):
#     if i %2==0:
#         print(i)

# for i in range(1,50):
#     if i %2 !=0:
#         print(i)

# sum = 0
# for i in range(1,101):
#     sum +=i
# print(sum)

# n = int(input("enter the number"))
# for i in range(1,11):
#     print(f"{i}*{n}={i*n}")

# n = int(input("enter the number"))
# fact = 1
# for i in range(1,n+1):
#     fact *=i
# print(fact)

# count = 0
# for i in range(1,101):
#     if i %3==0:
#         count += 1
# print(count)

# n = int(input("enter a number:"))
# reverse = 0
# temp = n
# for i in range(len(str(n))):
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp //=10
# print(reverse)

# sum = 0
# for i in range(1,101):
#     if i %2==0:
#         sum +=i
# print(sum)

# n = int(input("enter the number"))
# for i in range(1,11):
#     print(f"{i}*{i}={i*i}")



# i =1
# while i <= 10:
#     print(i)
#     i += 1

# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

# n = int(input("enter the number"))
# i = 1
# while i <= 10:
#     print(f"{i}*{n}={i*n}")
#     i += 1

# n = int(input("enter the number"))
# fact = 1
# i = 1
# while i <= n:
#     fact *=i
#     i += 1
# print(fact)

# i = 20
# while i >= 1:
#     print(i)
#     i -=1

# n = int(input("enter the number"))
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print(count)

# n = int(input("enter the number"))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
# print(sum)

# n = int(input("enter the number"))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n // 10
# print(reverse)



# a = int(input ("enter a number : "))
# number =0
# while a!=0:
#     number=number+a
#     a = int(input ("enter a number : "))
# print(number)


# while True:
#     print("1. add")
#     print("2. Sub")
#     print("3. Mul")
#     print("4. div")
#     print("5. Exit")

#     choice  = int(input("enter your choice : "))

#     if choice ==1:
    #     number1 = int(input("enter your first number : "))
    #     number2 = int(input("enter your second number : "))
    #     answer = number1+number2
    #     print(answer)
    # elif choice ==2:
    #         number1 = int(input("enter your first number : "))
    #         number2 = int(input("enter your second number : "))
    #         answer = number1-number2
    #         print(answer)

    # elif choice ==5:
    #      break



# std={}
# while True:
#     print("1.add student")
#     print("2.view student")
#     print("3.update student")
#     print("4.delete student")
#     print("5.view all student")
#     print("6.exit")

#     choice = int(input("enter your choice :"))

#     if choice == 1:
#         d={}
        # name = input("enter the name :")
        # phonenumber = int(input("enter the phone number :"))
        # email = input("enter the email :")
        # age = int(input("enter the age :"))
        # city = input("enter the city :")
        # d["name"]=name
        # d["phone"]=phonenumber
        # d["email"]=email
        # d["age"]=age
        # d["city"]=city
        # l.append(d)
        # print(d)
        # print(l)

    # elif choice == 2:
    #     search = input("enter phone number to search :")
    #     for i in l:
    #         if i["phonenumber"] == search:
    #             print(i)       
        


std={}
while True:
    print("1.add student")
    print("2.view student")
    print("3.update student")
    print("4.delete student")
    print("5.view all student")
    print("6.exit")

    choice=int(input("enter your choice:"))

    if choice==1:
        phn_no=int(input("enter your phone number:"))
        if phn_no in std:
            print("phone number already exists!")
            continue

        name=str(input("enter your name:"))
        age=int(input("enter your age:"))
        email=str(input("enter your email id:"))
        city=str(input("enter your city:"))
        std[phn_no]={"name" : name, "phone number" : phn_no, "age" : age, "email" : email, "city" : city}
        print("student added successfully!")

    elif choice==2:
        phn_no=int(input("enter the phone number:"))
        if phn_no in std:
            print(f"name : {std[phn_no]['name']}")
            print(f"phone number : {std[phn_no]['phone number']}")
            print(f"age : {std[phn_no]['age']}")
            print(f"email : {std[phn_no]['email']}")
            print(f"city : {std[phn_no]['city']}")
        else:
            print("student data not found!")

    elif choice==3:
        phn_no=int(input("enter the number:"))
        if phn_no in std:
            print("if you dont have anything to update, please press enter")
            i=std[phn_no]
            new_name=str(input("enter the changed name:"))
            new_age=input("enter the changed age:")
            new_email=str(input("enter the updated email:"))
            new_city=str(input("enter the changed city:"))

            if new_name:i['name']=new_name
            if new_age:i['age']=int(new_age) 
            if new_email:i['email']=new_email
            if new_city:i['city']=new_city
            print("student details updated successfully!")
        else:
            print("not found!")

    elif choice==4:
        phn_no=int(input("enter the phone number of the student that need to be removed:"))

        if phn_no in std:
            del std[phn_no]
            print("student data is deleted")
        else:
            print("student phone number mismatched!")

    elif choice==5:
        for phn,s in std.items():
            print(f"name : {s['name']}")
            print(f"phone number : {s['phone number']}")
            print(f"age : {s['email']}")
            print(f"email : {s['email']}")
            print(f"city : {s['city']}")
        else:
            print("no student records found!")
    else:
        break     

        