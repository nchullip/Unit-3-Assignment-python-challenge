######################################################################
# main.py : This script is used for computing various values within
#           a given Dataset in the form of CSV document.
#           This script displays the output on the Terminal and also
#           creates a Text Document with the output.
######################################################################

# Importing Modules
import os, csv

# Initializing Variables
month_counter = 0
net_amount = 0
temp_amount = 0
check = True
change = 0
max_profit_amt = 0
max_loss_amt = 0
max_profit_month = ""
max_loss_month = ""

# Fetching the Dataset
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
	# Creating the  CSV reader object
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader, None)

	# Traversing through each row in the CSV
	for row in csvreader:
		month = row[0]
		amount = int(row[1])

		if month != "":
			if check == False:
				# Computing Maximum Profit and Loss across the Dataset
				if ((amount - temp_amount) > max_profit_amt):
					max_profit_amt = amount - temp_amount
					max_profit_month = month
				elif ((amount - temp_amount) < max_loss_amt):
					max_loss_amt = amount - temp_amount
					max_loss_month = month

				# Adding the change in Profit/Losses	
				change += amount - temp_amount

			temp_amount = amount
			month_counter += 1
			net_amount += amount
			check = False
		else:
			# Breaking out of the Loop incase of Blank Cell
			break

# Creating Output Directory
if not os.path.exists("Output"):
	os.makedirs("Output")

# Creating Output Text Document and populating output values
f= open("Output/Financial_Anlaysis.txt","w+")
f.write("Financial Analysis \n")
f.write("------------------------------------- \n")
f.write("Total Months: " + str(month_counter) + "\n")
f.write("Total: $" + str(net_amount) + "\n")
message = "Average Change: $" + str(round(change/(month_counter-1), 2)) + "\n"
f.write(message)
message = "Greatest Increase in Profits: " + str(max_profit_month) + " ($" + str(max_profit_amt) + ")\n"
f.write(message)
message = "Greatest Decrease in Profits: " + str(max_loss_month) + " ($" + str(max_loss_amt) + ")\n"
f.write(message)
f.close()

# Display Output on the Terminal
print ("Financial Analysis")
print ("-------------------------------------")
print (f"Total Months: {month_counter}")
print (f"Total: ${net_amount}")
print (f"Average Change: ${str(round(change/(month_counter-1), 2))}")
print (f"Greatest Increase in Profits: {max_profit_month} ($ {max_profit_amt})")
print (f"Greatest Decrease in Profits: {max_loss_month} ($ {max_loss_amt})")
