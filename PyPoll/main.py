import csv
with open("election_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    total_votes = (len(votes))

    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
     
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

print ("Election Results")
print ("-------------------------")
print("Total Votes: ", total_votes)
print ("-------------------------")
print ("Khan: ", khan_percent, "% ", "(", khan_votes, ")")
print ("Correy: ", correy_percent, "% ", "(", correy_votes, ")")
print ("Li: ", li_percent, "% ", "(", li_votes, ")")
print ("O'Tooley: ", otooley_percent, "% ", "(", otooley_votes, ")")
print ("-------------------------")
print ("Winner: ", winner)
print ("-------------------------")