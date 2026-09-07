import pandas as pd

# data = {
#     'Name': ['Shailesh', 'Bakugo', 'Naruto', 'Eren'],
#     'Age': [25, 30, 35, 40],
# }

# df = pd.DataFrame(data)
# print(df.loc[0])
# print(df.loc[[0,1]])
# print(df)

# ls = ['Shailesh', 'Bakugo', 'Naruto', 'Eren']
# series = pd.Series(ls,index=["1","2","3","4"])
# print(series["1"])
# print(series)


df = pd.read_csv('data.csv')
# print(df.head(4))
# print(df.tail(3))
# print(df.info())


# data cleaning

# # remove null valued records
# df.dropna(inplace=True)
# print(df.to_string())

# replace value with mean 
avg_calories = df["Calories"].mean()
avg_maxpulse = df["Maxpulse"].mean()
df.fillna({"Calories": avg_calories,"Maxpulse": avg_maxpulse},inplace=True)
# print(df.to_string())

# wrong format data 
df["Date"] = pd.to_datetime(df['Date'],format="mixed")
# print(df.to_string())

# remove only data with date = NaT
df.dropna(subset=['Date'], inplace = True)

# replacing wrong data 

for i in df.index:
    if df.loc[i,"Duration"] > 200:
        df.loc[i,"Duration"] = 80

print(df.to_string())


# print true is row is occurred before 
# print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df.to_string())

