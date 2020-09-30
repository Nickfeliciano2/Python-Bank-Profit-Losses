import csv 

with open("budget_data.csv", newline="") as file:
    reader = csv.reader(file, delimiter=',')
    csv_header = next(reader)
    month = []
    gross = []
    gross_change = []
    monthly_change = []
                       
    for row in reader:
        month.append(row[0])
        gross.append(row[1])
    gross_int = map(int,gross)
    total_gross = (sum(gross_int))

    i = 0
    for i in range(len(gross) - 1):
        profit_loss = int(gross[i+1]) - int(gross[i])
        gross_change.append(profit_loss)
    Total = sum(gross_change)
    monthly_change = Total / len(gross_change)
    
    profit_increase = max(gross_change)
    j = gross_change.index(profit_increase)
    month_increase = month[j+1]
    profit_decrease = min(gross_change)
    k = gross_change.index(profit_decrease)
    month_decrease = month[k+1]

print ("Financial Analysis")
print ("----------------------------")
print("Total Months: ", len(month))
print (f"Total: ${total_gross}")
print (f"Average Change: ${round(monthly_change,2)}")
print (f"Greatest Increase in Profits: {month_increase} ( ${profit_increase} )")
print (f"Greatest Decrease in Profits: {month_decrease} ( ${profit_decrease} )")