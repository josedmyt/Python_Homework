import os
import csv
import statistics

bank_path= os.path.join("C:/Users/josed/Desktop/UT-TOR-DATA-PT-01-2020-U-C/03-Python/Instructions/PyBank/Resources/budget_data.csv")
#bank_path= os.path.join("C:","Users","josed","Desktop","UT-TOR-DATA-PT-01-2020-U-C","03-Python","Instructions","PyBank","Resources","budget_data.csv")

months=[]
profit_losses=[]
changes_profit=[]

lastrow=0

with open(bank_path,newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header=next(reader)
    for row in reader:
        months.append(str(row[0]))
        profit_losses.append(int(row[1]))
        change= (int(row[1]) - lastrow)
        changes_profit.append(change)
        lastrow=int(row[1])
    changes_profit.pop(0)

    total_months= len(months)
    net_profit_loss= sum(profit_losses)
    average_change= round(statistics.mean(changes_profit),2)
    max_profit = max(changes_profit)
    max_profit_month = months[changes_profit.index(max_profit)+1]
    max_loss = min(changes_profit)
    max_loss_month = months[changes_profit.index(max_loss)+1]

    print(total_months)
    print(net_profit_loss)
    print(average_change)
    print(max_profit)
    print(max_profit_month)
    print(max_loss)
    print(max_loss_month)


outpath= "Desktop/Homework/Python_Homework/PyBank/Analysis.txt"

with open(outpath,'w',newline='') as text:
    print("Financial Analysis", file=text)
    print("--------------------------",file=text)
    print(f"Total Months: {total_months}", file=text)
    print(f"Total: ${net_profit_loss}", file=text)
    print(f"Average Change: ${average_change}", file=text)
    print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})", file=text)
    print(f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})", file=text)
    print("--------------------------", file=text)
