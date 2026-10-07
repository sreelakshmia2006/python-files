from cal_answer import add,sub,mul,div

while True:
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.exit")

    choice = int(input("enter your choice :"))

    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        break
    else:
        print("invalid")
        

    
    
