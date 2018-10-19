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

        

               
#Display results to screen
print("Financial Analysis")
print(" ----------------------------")
print(f"Total months: {monthCount}")
print(f"Total: ${netTotal}")
print(f"Greatest Increase in Profits: {greatestProfitIncreaseMonth} (${greatestProfitIncreaseAmount})")
print(f"Greatest Decrease in Profits: {greatestProfitDecreaseMonth} (${greatestProfitDecreaseAmount})")
       

#Write results to text file
	
#path to output text file
txt_output = os.path.join("Output", "PyBank_text_output.txt")

#Open file in write mode and specify variable to hold contents
with open(txt_output, 'w', newline = "") as txt_file:
	#initialize txt writer
	txt_file.write(f"Financial Analysis\n")
	txt_file.write(f"----------------------------\n")
	txt_file.write(f"Total months: {monthCount}\n")
	txt_file.write(f"Total: ${netTotal}\n")
	txt_file.write(f"Greatest Increase in Profits: {greatestProfitIncreaseMonth} (${greatestProfitIncreaseAmount})\n")
	txt_file.write(f"Greatest Decrease in Profits: {greatestProfitDecreaseMonth} (${greatestProfitDecreaseAmount})\n")
 
#Open file for writing (basic write)          
#file = open("PyBank_output.txt","w")

#file.write(f"Total months: {monthCount}")   
#file.write(f"Total: {netTotal}")
#file.write(f"Greatest Increase in Profits: {greatestProfitIncreaseMonth} (${greatestProfitIncreaseAmount})")
#file.write(f"Greatest Decrease in Profits: {greatestProfitDecreaseMonth} (${greatestProfitDecreaseAmount})")
