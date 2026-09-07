import pandas as pd

df = pd.read_csv("data.csv")

# 1. total unique rows
print(df["Transaction_ID"].nunique())

# 2. Category Count
total_categories = df["Product_Category"].value_counts()
max_freq = total_categories.max()
most_freq = total_categories[total_categories == max_freq].index.tolist()

print(most_freq)

# 3. High ratings 
high_ratings = df[df["Rating"] >= 4.5]
print(high_ratings)

# 4. Avg ratings
print(df["Rating"].mean())

# 5. Top 5 most costly products
sorted_df = df.sort_values(by="Unit_Price",ascending=False)
print(sorted_df.head(5).to_string())

# 6. Calculating total
df["Raw_Total"] = df["Quantity"] * df["Unit_Price"]
print(df[['Transaction_ID', 'Raw_Total']].head(3))

# 7. Specific category and Quantity count
print(df[(df["Product_Category"] == "Electronics") & (df["Quantity"] >= 2)].to_string())

# 8. Product category vise rating mean
print(df.groupby("Product_Category")["Rating"].mean())

# 9. Transactions for specific payment type
print(df[df["Payment_Method"].isin(["PayPal","Cash"])])

# 10. Print Transaction date
df["Date"] = pd.to_datetime(df["Date"])
print(df["Date"].dt.day_name().head(3).to_string())

# 11. Most recent Transactions
print(df.sort_values(by="Date", ascending=False).head(3))

# 12. Giving Premium user discount
df.loc[df["Customer_Type"] == "Premium","Discount_Pct"] = 0.25
print(df[['Customer_Type', 'Discount_Pct']].head(3))

# 13. Aggregation of price
print(df.groupby("Product_Category")["Unit_Price"].agg(["min","max","mean"]))