import csv
import random

def cud():
	deck = []
	hand = []
	play = 0
	oppplay = 0
	opphand = []
	oppcard = ''
	with open("nwlist.csv", "r") as file:
		csvr = csv.DictReader(file)
		for row in csvr:
			deck.append(row)
	print("User turn: ")
	for i in range(0,3):
		x = random.randint(0,len(deck)-1)
		hand.append(deck[x]['name'])
	print(hand)
	mp1 = int(input("Pick one card: (0 | 1 | 2) \n:"))
	choos = hand[mp1]
	for i in deck:
		if i['name'] == choos:
			play += int(i['strength'])
	print(f"Your card has a strength of {play}")
	for i in range(0,3):
		x = random.randint(0,len(deck)-1)
		opphand.append(deck[x]['name'])
	cpu = random.randint(0,2)
	cpuchoice = opphand[cpu]
	for i in deck:
		if i['name'] == cpuchoice:
			oppplay += int(i['strength'])
			oppcard = i['name']
	if play > oppplay:
		print(f"John played {oppcard} with strength of {oppplay}")
		print("You win!")
	else:
		print(f"John played {oppcard} with strength of {oppplay}")
		print("You lose!")
	


