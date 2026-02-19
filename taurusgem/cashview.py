import csv
import datetime
import pandas as pd
from tabul import dataview
import matplotlib.pyplot as plt
def transact():
	list1 = []
	tran = int(input("Number of transactions: "))
	i = 0
	while i < tran:
		mkey = input("Enter a transaction name: ")
		mval = int(input("Enter the transaction amount: "))
		date = str(datetime.datetime.now())[0:10]
		with open('fmonth1.csv', 'a') as file:
			file.write(f"{date},{mkey},{mval} \n")
		with open('fmonth1.csv', 'r') as file:
			csvr = csv.DictReader(file)
			for row in csvr:
				list1.append(row)
			for x in range(0,len(list1)):
				for y in list1[x]:
					if y == 'Cost':
						list1[x][y] = float(list1[x][y]) #reassign cost values to float for all item in list
		i+=1
def tview():
	list1 = []
	list2 = []
	with open('fmonth1.csv', 'r') as file:
		csvr = csv.DictReader(file)
		for row in csvr:
			list1.append(row)
		for i in range(0,len(list1)):
			list2.append(int(list1[i]['Cost']))
		x = sum(list2)
		frame = pd.DataFrame(list1)
		print("Your Credit Card transactions for your main account: \n")
		print(frame)
		print(f"\n Total extra expenses for the current month: {x} \n")
		print(f"\n Total Overall expenses for the current month: {x+55} \n")
def tview2():
	list1 = []
	list2 = []
	list3 = []
	with open('fmonth1.csv', 'r') as file: #modify this line to change the monthly view
		csvr = csv.DictReader(file)
		for row in csvr:
			list1.append(row)
		for i in range(0,len(list1)):
			list2.append(int(list1[i]['Cost']))
		x = sum(list2)
		for i in range(0,len(list1)):
			list3.append(list1[i]['Date'])
		plt.figure(figsize=(8,5))
		plt.plot(list3, list2, color = 'blue')
		plt.xlabel('Date')
		plt.ylabel('Cost')
		plt.title('Finance View')
		plt.grid(axis='y', linestyle= '--', alpha=0.7)
		plt.show()
