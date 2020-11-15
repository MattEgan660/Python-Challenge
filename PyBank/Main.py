#Import Modules
import os 
import csv 
   
#Data lists 
months = []
revenue = []

#Read CSV
data = os.path.join('Resources', 'budget_data.csv')

with open(data, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    print(csvreader)

    #Loop through CSV
    for row in csvreader:
        months.append(row[0])
        revenue.append(float(row[1]))

#Total Months
total_months = (len(months))


#Total Profit
net_revenue = sum(revenue)

#Average change in Profit
avg_change = net_revenue / total_months


#Largest increase in profit
max_profit = max(revenue)
max_index = revenue.index(max_profit)
max_month = months[max_index]


#largest decrease in profit
min_profit = min(revenue)
min_index = revenue.index(min_profit)
min_month = months[min_index]


#Terminal Printout 
print("Financial Analysis")
print("-" * 30)
print(f"Months: {str(total_months)}")
print(f"Total: {str(net_revenue)}")
print(f"Average Change: {str(avg_change)}")
print(f"Greatest Increase in Profits: {str(max_month)} (${str(max_profit)})")
print(f"Greatest Decrease in Profits: {str(min_month)} (${str(min_profit)})")


#Output to .txt file
output_file= os.path.join('Analysis', "Output.txt")

with open(output_file, "w") as new:
    new.write("Financial Analysis\n")
    new.write("--------------------------------\n") 
    new.write(f"Months: {str(total_months)}\n")
    new.write(f"total: {str(net_revenue)}\n")
    new.write(f"Average Change: {str(avg_change)}\n")
    new.write(f"Greatest Increase in Profits: {str(max_month)} (${str(max_profit)})\n")
    new.write(f"Greatest Decrease in Profits: {str(min_month)} (${str(min_profit)})")
