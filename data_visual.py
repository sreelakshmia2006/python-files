    #-----DATA VISUALISATION-----

import matplotlib.pyplot as plt

# plt.plot([1,2,3],[10,20,30])                          # create a plot
# plt.show()                                            # show is used to show the chart


     #-----LINE PLOT-----                                  # trend over peroid
# Months = ["Jan","Feb","Mar","Apr"]           
# Sales = [20000,25000,30000,28000]
# plt.plot(Months,Sales)
# plt.title("Monthly Sales Trend")                         # give title for the graph
# plt.xlabel("Month")                                      # x-axis label
# plt.ylabel("Sales")                                      # y-axis label
# plt.show()

# plt.plot(Months,Sales,marker="o",color="red",linestyle="--")                
# plt.show()

     #-----SCATTER-----
# sales = [20000,30000,40000,50000]                           # understand the relationship between variables
# profit = [3000,6000,9000,12000]
# plt.scatter(sales,profit)                                  # create ascatter plot
# plt.title("Sales vs Profit")
# plt.xlabel("sales")
# plt.ylabel("profit")
# plt.show()

# plt.scatter(sales,profit,color="green",marker="x",s=100)                      # changes the point color,point-x symbol,s is size of marker
# plt.show()

     #-----BAR-----
# regions = ["North","South","East","West"]                          # compare cheyyan use cheyunnu barchart
# sales = [40000,35000,30000,45000]
# plt.bar(regions,sales,color="red",width=0.5)                                                  # create bar chart verticaly
# plt.title("Sales by Region")
# plt.xlabel("region")
# plt.ylabel("sales")
# plt.show()

# plt.barh(regions,sales,color="red",height=0.5)                                                # create bar chart horizondaly
# plt.show()

     #-----PIE-----
# labels = ["product A","product B","product C"]                      # proportion or percentage nokan
# sales = [50,30,20]
# plt.pie(sales, labels=labels, autopct="%1.1f%%",explode=[0.1,0,0],startangle=90)
# plt.title("Market Share")
# plt.show()


# marks = [45,55,60,65,70,75,80,85,90,95]                            # distribution of data 
# plt.hist(marks,bins=5)
# plt.title("Marks Distribution")
# plt.xlabel("marks")
# plt.ylabel("number of students")
# plt.show()

     #-----BOXPLOT-----
# salaries = [25000,30000,32000,40000,100000]                            # botplot used to show spred & outliers
# plt.boxplot(salaries)
# plt.title("Salary Distribution")
# plt.ylabel("salary")
# plt.show()
