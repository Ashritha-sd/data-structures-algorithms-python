expenses=[2200, 2350, 2600, 2130, 2190]
#1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, how many dollars I spent extra compare to January : ", expenses[1]-expenses[0])
#2. Find out your total expense in first quarter (first three months) of the year.
print("Total expense in first quarter i.e, first 3 months", expenses[0]+expenses[1]+expenses[2])
#3. Find out if you spent exactly 2000 dollars in any month
print("Did I spend exactly 2000 in any month?", 2000 in expenses)
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print("Expenses Jan-Jun : ",expenses)
#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expenses[3]=expenses[3]-200
print("Updated April expense : ",expenses[3])