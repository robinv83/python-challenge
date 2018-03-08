import os
import csv

csvpath = os.path.join(r"C:\Users\Admin\Desktop\UNCCHAR201802DATA2-Class-Repository-DATA\Homework\Week-03-Python\Instructions\PyPoll\raw_data\election_data_1.csv")


row_count = 0
mydict = {}
with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    #next(csv_reader)
    mydict = {rows[0]: rows[2] for rows in csv_reader}
    for rows in mydict:
        print(rows, mydict[rows])



    




