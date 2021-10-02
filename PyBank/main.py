import os
import csv

#path to collect the data from the budget data csv file
csvpath = os.path.join('resources/budget_data.csv')

TotalMonths = 0
TotalAmount = 0
monthlyChange =[]
months= []

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)

    #To read the header row
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    firstRow = next(csv_reader)

    #Add the count of the total months
    TotalMonths = TotalMonths + 1 

    #Add the total amount of "Profit/Losses"
    TotalAmount += float(firstRow[1])

    #Establishing previous profit/losses column
        #Profits/Losses are located in index 1
    previousNetChange = float(firstRow[1])
    
    #Calculate the total number of months 
    for row in csv_reader:
        TotalMonths = TotalMonths + 1 
        print(row)
    
    #calculate the  total amount of "Profit/Losses" over the entire period
        TotalAmount += float(row[1])


    #calculate the changes in "profit/Losses" over the entire period
        netChange = float(row[1]) - previousNetChange
        #add on to list of average changes
        monthlyChange.append(netChange)

        #add the first month that a change occurred
        months.append(row[0])

        #update previous net change
        previousNetChange = float(row[1])
#Calculate the Average of the monthly changes
averageChange = sum(monthlyChange) / len(monthlyChange)

greatestIncrease = [months[0], monthlyChange [0]]
greatestDecrease = [months[0], monthlyChange [0]]

    #calculate the greatest increase in profits (date and amount) over the entire period

for m in range(len(monthlyChange)):
    if(monthlyChange[m]> greatestIncrease[1]):
            greatestIncrease[1] = monthlyChange[m]
            #update the month 
            greatestIncrease [0] = months [m]
    #Calculate the greatest decrease in profits (date and amount) overthe entire period 
    if(monthlyChange[m]< greatestDecrease[1]):
            greatestDecrease[1] = monthlyChange[m]
            #update the month 
            greatestDecrease [0] = months [m]
#Creating output for the data
output = (
     f"\n Financial Analysis \n"
     f"------------------------ \n"
     f"Total Months = {TotalMonths}\n"
     f"Total =${TotalAmount:,.2f}\n"
     f"Average Change = ${averageChange:,.2f}\n"
     f"Greatest Increase in Profits = {greatestIncrease[0]} (${greatestIncrease[1]:,.2f}) \n"
     f"Greatest Decrease in Profits = {greatestDecrease[0]} (${greatestDecrease[1]:,.2f})\n"
 )
#print the output 
print(output)

#Write results in to a text file
mainFile = os.path.join('PyBank.txt')

with open(mainFile,"w") as textfile:
    textfile.write(output)




