# normal way 
# with open("data.csv" , "r") as file:
#     data = file.read().split(",")
#     print(data)
#     print(f"{data[0]} |  {data[1]}")
#     print(f"{data[2]} |  {data[3]}")


# using csv module
import csv 


with open("data.csv" , "r+") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    
    for data in reader:
        if len(data) >= 2:
            print(f"Name: {data[0]} , Age : {data[1]}")
        
    file.seek(0)
    
    data = [
        ["Name", "Age", "Role"],
        ["Shailesh", "20", "Intern"],
        ["Meet", "30", "Designer"]
    ]
    
    writer = csv.writer(file)
    writer.writerows(data)
