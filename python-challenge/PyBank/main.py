#Import modules
import os
import csv
csvpath = os.path.join('budget_data.csv')

#List Variables
months = 0
net = 0
Average_Change = 0
Greatest_Profit = 0
Greatest_Loss = 0
Greatest_Profit_Month = []
Greatest_Loss_Month = []

# Loop thru file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    next(csvreader, None)
            
    # Get data
    row = next(csvreader,None)
    months = 1
    revenue = int(row[1])
    net = int(row[1])
    Greatest_Profit = revenue
    Greatest_Profit_Month = (row[0])
    Greatest_Loss = revenue
    Greatest_Loss_Month = (row[0])
        
    # Read one row at a time
    for row in csvreader:

        # Increase month
        months = months + 1

        # Add to revenue to net
        revenue = int(row[1])
        net = net + revenue

        # Determine if revenue is > or < peaks
        if revenue > Greatest_Profit:
            Greatest_Profit_Month = (row[0])
            Greatest_Profit = revenue

        if revenue < Greatest_Loss:
            Greatest_Loss_Month = (row[0])
            Greatest_Loss = revenue

    # Calculate Mean
    Average_Change = int(net/months)
     
# Print analysis
print("Financial Analysis")
print("----------------------")
print("Total Months:")
print(months)
print("Total (USD):") 
print(net)
print("Average Change (USD):")
print(Average_Change)
print("Greatest Profits (Month):") 
print(Greatest_Profit_Month)
print("Greatest Profits (USD):") 
print(Greatest_Profit)
print("Greatest Loss (Month):") 
print(Greatest_Loss_Month)
print("Greatest Loss (USD):") 
print(Greatest_Loss)

# Output to txt
filepath = os.path.join("output","financial_analysis_.txt")
with open(filepath, "w") as writefile:
    writefile.writelines("Financial Analysis"+ '\n')
    writefile.writelines("----------------------"+ '\n')
    writefile.writelines("Total Months:"+ '\n')
    writefile.writelines(str(months)+ '\n')
    writefile.writelines("Total (USD):"+ '\n') 
    writefile.writelines(str(net)+ '\n')
    writefile.writelines("Average Change (USD):"+ '\n')
    writefile.writelines(str(Average_Change)+ '\n')
    writefile.writelines("Greatest Profits (Month):"+ '\n') 
    writefile.writelines(str(Greatest_Loss_Month)+ '\n')
    writefile.writelines("Greatest Profits (USD):"+ '\n') 
    writefile.writelines(str(Greatest_Profit)+ '\n')
    writefile.writelines("Greatest Loss (Month):"+ '\n') 
    writefile.writelines(str(Greatest_Loss_Month)+ '\n')
    writefile.writelines("Greatest Loss (USD):"+ '\n') 
    writefile.writelines(str(Greatest_Loss)+ '\n')