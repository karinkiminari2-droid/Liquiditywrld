#tabulate test
#takes a dictionary and creates a table to view that info
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
def dataview(dictate):
	if dictate:
		for k,v in dictate.items():
			u = list()
			u.append(v)
			dictate[k] = u
		edictview = pd.DataFrame(dictate)
		print("-----------------")
		print(edictview)
		print("----------------")
	else:
		pass#if there's nothing in the dictionary, dictate, just do nothing and move on


