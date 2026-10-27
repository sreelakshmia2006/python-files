# import numpy as np
# print(np.__version__)


# import numpy as np                                               #np.array
# numbers = np.array([10,20,30,40,50])
# print(numbers)
# print(type(numbers))

# import numpy as np
# a= np.zeros(5)
# print("zeros:",a)

# b= np.ones(5)
# print("ones:",b)

# c= np.arange(1,11)                                           # range use
# print("Range:",c)

# d= np.arange(2,21,2)                                         
# print("Range with step:",d)

# e= np.arange(1,21,2)
# print("Range with step:",e)

# f= np.linspace(1,10,3)                                    #linspace()-generates a specified number of evenly spaced values
# print("Linspace:",f)


# a=np.array([10,20,30,40])

# b=np.array([
#     [10,20,30],
#     [40,50,60]
# ])

# print("1D Array:")
# print(a)

# print("2D Array:")
# print(b)

# print("Dimensions:",a.ndim)
# print("shape:",a.shape)
# print("total elements:",a.size)

# print("Dimensions:",b.ndim)
# print("shape:",b.shape)
# print("total elements:",b.size)               # shape returns number of rows & columns while size return total number of elements.

# a=np.array([10,2,30])                           # data type
# b=np.array([1.5,2.5,3.5])
# c=np.array([True,False,True])
# z=np.zeros(5)

# print(a.dtype)
# print(b.dtype)
# print(c.dtype)
# print(z.dtype)



# marks=np.array([75,82,68,91,88])
# print("First mark:",marks[0])
# print("Third mark:",marks[2])
# print("Last mark:",marks[-1])

# marks[1] = 95
# print("Updated marks:",marks)




# a=np.linspace(0,100,5)
# print("linspace:",a)



# import numpy as np
# marks=np.array([75,82,68,91,88])
# print("marks:",marks)
# zeros = np.zeros(5)
# print("zeros:",zeros)
# ones = np.ones(5)
# print("ones:",ones)
# array = np.arange(10,21)
# print("10 to 20:",array)
# even = np.arange(2,21,2)
# print("even 2 to 20:",even)
# a = np.linspace(0,100,5)
# print("linspace:",a)




# import numpy as np
# student_marks= np.array([
#     [75,82,68],
#     [91,88,95],
#     [65,72,80]
# ])
# print(student_marks)



# import numpy as np
# print("1.dimensions:",student_marks.ndim)
# print("2.shape:",student_marks.shape)
# print("3.total elements:",student_marks.size)
# print("4.data type:",student_marks.dtype)



# print("1.first mark:",marks[0])
# print("2.third mark:",marks[2])
# print("3.lsat mark:",marks[-1])
# print("4.second_last marks:",marks[-2])
# marks[1]=90
# marks[-1]=95
# print("5 & 6. after changing 2nd to 90 and last to 95:")
# print("7. updated array:",marks)




# ages = np.array([18,20,19,21,18])
# print("1.first age:",ages[0])
# print("2.last age:",ages[-1])
# ages[2]=22
# print("3.changed 3rd student age to 22")
# print("4.updated array:",ages)
# print("shape:",ages.shape)
# print("size:",ages.size)
# print("dimensions:",ages.ndim)
# print("datatypes:",ages.dtype)



import numpy as np
students = {
    "Anu": {"Python": 75, "SQL": 82, "Excel": 68},
    "Rahul": {"Python": 91, "SQL": 88, "Excel": 95},
    "Priya": {"Python": 65, "SQL": 72, "Excel": 80}
}

def display_all():
    print("\n--- Display All Students ---")
    for name, marks in students.items():
        print(name, "->", marks)

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print(name, "found:", students[name])
    else:
        print("Student", name, "not found!")

def total_average():
    print("\n--- Total and Average ---")
    for name, marks in students.items():
        total = sum(marks.values())
        avg = total / 3
        print(name, "-> Total:", total, "Average:", round(avg, 2))

def find_topper():
    print("\n--- Find Topper ---")
    topper = max(students, key=lambda n: sum(students[n].values()))
    total = sum(students[topper].values())
    print("Topper is", topper, "with Total", total)

def update_marks():
    name = input("Enter student name: ")
    if name in students:
        subject = input("Enter subject (Python/SQL/Excel): ")
        if subject in students[name]:
            new_mark = int(input("Enter new mark: "))
            students[name][subject] = new_mark
            print("Updated!")
        else:
            print("Invalid subject!")
    else:
        print("Student not found!")

def add_new_student():
    name = input("Enter new student name: ")
    py = int(input("Enter Python mark: "))
    sql = int(input("Enter SQL mark: "))
    excel = int(input("Enter Excel mark: "))
    students[name] = {"Python": py, "SQL": sql, "Excel": excel}
    print("Student", name, "added!")

def subject_wise_topper():
    print("\n--- Subject-wise Topper ---")
    for subject in ["Python", "SQL", "Excel"]:
        topper = max(students, key=lambda n: students[n][subject])
        print(subject, "Topper:", topper, students[topper][subject])

while True:
    print("1. Display All")
    print("2. Search Student")
    print("3. Total and Average")
    print("4. Find Topper")
    print("5. Update Marks")
    print("6. Add New Student")
    print("7. Subject-wise Topper")
    print("8. Exit")
    choice = input("Enter choice (1-8): ")
    if choice == "1":
        display_all()
    elif choice == "2":
        search_student()
    elif choice == "3":
        total_average()
    elif choice == "4":
        find_topper()
    elif choice == "5":
        update_marks()
    elif choice == "6":
        add_new_student()
    elif choice == "7":
        subject_wise_topper()
    elif choice == "8":
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice!")





















