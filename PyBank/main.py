import os
import csv

#path to the csv file
bank_csv = os.path.join("Resources","budget_data.csv")

#open the file 
with open (bank_csv, newline="") as bankcsvfile:
	#create a reader to the file
	csv_reader = csv.reader(bankcsvfile, delimiter = ",") 
    
	csv_header = next(csv_reader)
	#print (f"The csv header is {csv_header}")
    
	#Variable Initialization
	monthCount = 0 
	netTotal = 0

	greatestProfitIncreaseMonth = ''
	greatestProfitIncreaseAmount = 0

	greatestProfitDecreaseMonth = ''
	greatestProfitDecreaseAmount = 0

    
    
	for row in csv_reader: #for each row in the csv file 
		#count #months in csv file
		monthCount += 1
        
		#Assign the profit/loss amount and month of each row to variable
		RowAmount = int(row[1])
		RowMonth = row[0]
        
		#total net amount of "Profit/Losses"
		netTotal = netTotal + RowAmount #2nd column => Profit/Loss column
        
		#greatest increase in profits (date & amount)
		if RowAmount > 0: #profit
			if RowAmount > greatestProfitIncreaseAmount: #New higher profit
				greatestProfitIncreaseAmount = RowAmount
				greatestProfitIncreaseMonth = RowMonth

		#greatest decrease in profits (date & amount)
		else: #loss
			if RowAmount < greatestProfitDecreaseAmount: #New lower profit
				greatestProfitDecreaseAmount = RowAmount
				greatestProfitDecreaseMonth = RowMonth

        
               
	#Display results
	print(f"Total months: {monthCount}")
	print(f"Total: {netTotal}")
	print(f"Greatest Increase in Profits: {greatestProfitIncreaseMonth} (${greatestProfitIncreaseAmount})")
	print(f"Greatest Decrease in Profits: {greatestProfitDecreaseMonth} (${greatestProfitDecreaseAmount})")
       
