# class Bank:                                                            # without encapsulation
#     def __init__(self):
#         self.balance=1000

# account=Bank()
# account.balance=-5000
# print(account.balance)



# class Bank:
#     def __init__(self):
#         self.__balance=1000
#     def set_balance(self,amount):
#         if amount>=0:
#             self.__balance=amount

#     def get_balance(self):
#         return self.__balance
# account=Bank()
# account.set_balance(-5000)
# print(account.get_balance())



# class Bank:
#     def __init__(self):
#         self.__balance=1000
#     @property
#     def balance(self):
#         return self.__balance
#     @balance.setter
#     def balance(self,amount):
#         if amount >=0:
#             self.__balance=amount
#         else:
#             print("Invalid balance. Balance cannot be negative")
# account=Bank()
# print("initial balance:",account.balance)

# account.balance=5000
# print("updated balance:",account.balance)

# account.balance=-2000
# print("Final balance:",account.balance)





# for i in range(1,6):
#     a=i
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a=a+1
#     print()


l=[]
num=int(input("how many numbers want?"))
for i in range(num):
    number=int(input(f"enter your {i+1} number : "))
    l.append(number)
print(l)


    
