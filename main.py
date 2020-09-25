import csv 
with open("budget_data.csv") as file:
    csv_reader = csv.reader(file, delimiter=",")
    data = [x for x in csv_reader]
    print(file)