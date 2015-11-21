# The White Male Index
# This Python file converts the import .csv data to a .json file
# The resulting .json file can be visualized using d3.js

import csv

with open('tbf_fall2015.csv', 'rb') as f:
	reader = csv.reader(f)
	index = list(reader)

for i in index:
	print i[0]