# import pandas as pd
# dataset = {
#     "Sales" : [25000,30000,20000,40000,28000],
#     "Profit" :[5000,7000,4000,10000,6000]
#     }
# df=pd.DataFrame(dataset)
# print(df)
# print(df.describe())                   # descriptive statistics

# print(df["Sales"].count())

# print(df["Sales"].mean())

# print(df["Sales"].std())

# print(df["Sales"].min())
# print(df["Sales"].max())

# print(df["Sales"].median())

# print(df["Sales"].mode())

    # -----Sorting & Ranking Data-----
# print(df.sort_values(by="Sales"))                  # sort one column
# print(df.sort_values(by="Sales",ascending=False))
# print(df.sort_values(by=["Sales","Profit"],ascending=[False,True]))                         # sort by multiple columns

# df["Sales_Rank"] = df["Sales"].rank(ascending=False)                 # ranking
# print(df)

# top_sales=df.sort_values(by="Sales",ascending=False).head(3)                  # finf top records
# print(top_sales)

# print(df.tail(3))                   # bottom records

    # ------Group by operations------
# df["Region"]=["North","South","East","West","Southeast"]
# print(df)
# print(df.groupby("Region")["Sales"].sum())                  # basic groupby operation

# print(df.groupby("Region")["Sales"].mean())
# print(df.groupby("Region")["Sales"].min())
# print(df.groupby("Region")["Sales"].max())

# print(df.groupby("Region").agg({"Sales":"sum", "Profit":"mean"}))                   # multiple aggregations with agg()






               #------Task practical-----
    #-----step:1 create dataset-----
# data = {
#     "Employee":["Arun","Anu","Rahul","Meera","John",
#                 "Priya","David","Sara","Kevin","Neha",
#                 "Arun","Meera","John","Priya","David"
#                 ],
#     "Region":["North","South","West","North","South",
#               "West","North","South","West","North",
#               "South","West","North","South","West"
#               ],
#     "Product":["Laptop","Mobile","Tablet","Laptop","Mobile",
#                "Laptop","Tablet","Mobile","Laptop","Tablet",
#                "Mobile","Laptop","Tablet","Mobile","Laptop"
#                ],
#     "Sales":[45000,30000,25000,55000,35000,
#              60000,20000,40000,75000,15000,
#              32000,50000,28000,42000,65000
#              ],
#     "Profit":[9000,6000,5000,11000,7000,
#               12000,4000,8000,15000,3000,
#               6500,10000,5500,8500,13000
#               ],
#     "Quantity":[2,3,1,4,2,
#                 5,1,3,4,1,
#                 2,3,2,4,5
#                 ]
# }
# df=pd.DataFrame(data)
# print(df)

    #-----step2: Descriptive statistics-----
# print(df.head(5))                                    # first 5
# print(df.tail(5))
# print(df.describe())
# print("Total records:", df["Sales"].count())
# print("Average sales:", df["Sales"].mean())
# print("Highest sales:", df["Sales"].max())
# print("Lowest sales:", df["Sales"].min())
# print("Average profit:", df["Profit"].mean())
# print("Median sales:", df["Sales"].median())
# print("Std of sales:", df["Sales"].std())
# print("Mode sales:", df["Sales"].mode())

     #-----step3: sorting & ranking-----
# print(df.sort_values("Sales"))
# print(df.sort_values("Sales",ascending=False))
# top_sales = df.sort_values(by="Sales",ascending=False).head(5)
# print(top_sales)
# bottom_sales = df.sort_values(by="Sales",ascending=False).tail(3)
# print(bottom_sales)
# print(df.sort_values("Profit",ascending=False))
# print(df.sort_values(["Region","Sales"]))
# df["Sales_rank"] = df["Sales"].rank(ascending=False)
# print(df.sort_values("Sales_rank"))

     #-----step4: Groupby operations-----
# print(df.groupby("Region")["Sales"].sum())
# print(df.groupby("Region")["Sales"].mean())
# print(df.groupby("Region")["Sales"].max())
# print(df.groupby("Region")["Sales"].min())

# print(df.groupby("Region")["Profit"].sum())
# print(df.groupby("Region")["Quantity"].sum())
# print(df.groupby("Product")["Sales"].sum())
# print(df.groupby("Product")["Profit"].mean())

# print(df.groupby("Region").agg(total_sales=("Sales","sum"),avg_profit=("Profit","mean")))


    # remaining line 45-----

# df.corr(numeric_only=True)                          # correlation
# df["Sales"].corr(df["Profit"])
