# import pandas as pd

   #-----Food Delivery Business Data analysis-----

# data={
    # "order_id":[101,102,103,104,105,
    #             106,107,108,109,110,
    #             111,112,113,114,115
    #             ],
    # "city":["kochi","calicut","trivandrum","kochi",
    #         "calicut","kochi","trivandrum","calicut",
    #         "kochi","trivandrum","calicut","kochi",
    #         "trivandrum","calicut","kochi"
    #         ],
    # "category":["pizza","burger","biriyani","pizza","biriyani",
    #             "burger","pizza","biriyani","burger","pizza",
    #             "burger","biriyani","pizza","burger","biriyani"
    #             ],
    # "revenue":[1200,800,1500,1800,1100,
    #            950,1600,1300,750,2000,
    #            900,1700,1400,850,1900
    #            ],
    # "advertising":[200,100,300,250,150,
    #                120,280,220,100,350,
    #                130,300,240,110,320
    #                ],
    # "delivery_time":[30,25,45,35,40,
    #                  28,32,42,22,38,
    #                  26,43,33,24,39
    #                  ],
#     "customer_rating":[4.5,4.2,3.8,4.7,4.0,
#                        4.3,4.6,3.9,4.4,4.8,
#                        4.1,3.7,4.6,4.3,4.9
#                        ]
# }
# df=pd.DataFrame(data)
# print(df)

    # ---initial data exploration---
# print(df.head(7))
# print(df.tail(3))
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.describe())

    # ---descriptive statistics---
# print("Total revenue:",df["revenue"].sum())
# print("Avg revenue:",df["revenue"].mean())
# print("Avg advertising:",df["advertising"].mean())
# print("Max delivery time:",df["delivery_time"].max())
# print('Min delivery time:',df["delivery_time"].min())
# print("Median rating:",df["customer_rating"].median())
# print("Std rating:",df["customer_rating"].std())
# print("Mode rating:",df["customer_rating"].mode())
# print("Total advertising:",df["advertising"].sum())

    # ---sorting & ranking---
# print(df.sort_values(by="revenue",ascending=False))
# top_revenue=df.sort_values(by="revenue",ascending=False).head(5)
# print(top_revenue)

# bottom_revenue=df.sort_values(by="revenue",ascending=False).tail(4)
# print(bottom_revenue)
# print(df.sort_values(by="customer_rating",ascending=False))
# print(df.sort_values(by="delivery_time",ascending=True))
# df["revenue_rank"] = df["revenue"].rank(ascending=False)
# df["delivery_rank"] = df["delivery_time"].rank(ascending=True)
# print(df)

     #---groupby operations---
# print(df.groupby("city")["revenue"].sum())
# print(df.groupby("city")["customer_rating"].mean())
# print(df.groupby("city")["delivery_time"].mean())
# print(df.groupby("city")["advertising"].sum())
# print(df.groupby("category")["revenue"].sum())
# print(df.groupby("category")["revenue"].max())
# print(df.groupby("category")["customer_rating"].mean())

# print(df.groupby(["city","category"])["revenue"].sum())
# print(df.groupby(["city","category"])["delivery_time"].mean())
# print(df.groupby(["city","category"])["revenue"].sum().reset_index())

     #---multiple aggregations using agg()---
# print(df.groupby("city").agg({
#     "revenue":"sum",
#     "advertising":"mean",
#     "customer_rating":"mean",
#     "delivery_time":"mean"
# }))

     #---correlation---
# print(df.corr(numeric_only=True))
# print("advertising vs revenue:", df["advertising"].corr(df["revenue"]))
# print("delivery_time vs customer_rating:", df["delivery_time"].corr(df["customer_rating"]))
# print("revenue vs customer_rating:", df["revenue"].corr(df["customer_rating"]))