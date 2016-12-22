#How to delete the same emails from one file
from collections import OrderedDict

with open('emails.txt') as fin: #here we add our file, it must be .txt and all emails must be in one row
    lines = (line.rstrip() for line in fin)
    unique_lines = OrderedDict.fromkeys( (line for line in lines if line) )

for k in unique_lines.keys():
	print (k)