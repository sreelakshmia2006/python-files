import pandas as pd
# print("pandas version:", pd.__version__)                                                                                               

# data = pd.Series([10,20,30,40])
# print(data)
# print(type(data))


# ls = [10,20,30,40]
# print(ls)
# print(type(ls))


# marks = pd.Series([85,90,76,92,68])
# print("First mark:",marks[0])
# print("Average:",marks.mean())
# print("Maximum:",marks.max())


# marks = pd.Series(
#     [85,90,76,92],
#     index=["Anu","Binu","Ciya","David"]
# )
# print("Anu's mark:",marks["Anu"])
# print("Marks above 80:")
# print(marks[marks > 80])


# salary = {                                           #creating series from dictionary
#     "Anita": 50000,
#     "Rahul": 45000,
#     "Meera": 60000
# }
# salary_series = pd.Series(salary)
# print(salary_series)


# monthly_sales = pd.Series(
#     [25000,30000,28000],
#     index=["Jan","Feb","Mar"]
#         )

# print(monthly_sales["Jan"])                       #accessing data using index
# print(monthly_sales.iloc[0])

# print(monthly_sales["Jan":"Mar"])                   #slicing
# print(monthly_sales[0:2])

# print(monthly_sales + 5000)                           # arithmetic operations(broadcasting)

# print(monthly_sales.mean())                             # statistical operations
# print(monthly_sales.max())
# print(monthly_sales.min())

# high_sales = monthly_sales[monthly_sales > 26000]            # filtering series
# print(high_sales)




              #hands on activity
# salary = pd.Series(
#     [45000,52000,60000,48000],
#     index=["Emp1","Emp2","Emp3","Emp4"]
# )
# print(salary)
# print(salary["Emp2"])
# increased_salary = salary * 1.10
# print(increased_salary)
# print(salary.mean())
# print(salary.max())
# filtered = salary[salary >= 50000]
# print(filtered)




# data = {                                                    #dataframe
#     "Name": ["Anita","Rahul","Meera"],
#     "Age": [22,24,23],
#     "Course": ["Analytics","Python","Analytics"]
# }
# df = pd.DataFrame(data)
# print(df)
# print(type(data))
# print(df.head())                                  # to get first 5 row 
# print(df.tail())                                  # to get last 5 row
# print(df.shape)                                   # get shape
# print(df.columns)
# print(df.info())                                  # to get all details


# print(df["Name"])                                # selecting one column

# print(df[["Name","Course"]])                       # selecting multiple columns


# df = pd.read_csv("student.csv")                      # data imported in excel file(venda file il save) 
# print(df)
# print(df.head())