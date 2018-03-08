import os
import csv
from collections import Counter

csvpath = os.path.join(r"C:\Users\Admin\Desktop\UNCCHAR201802DATA2-Class-Repository-DATA\Homework\Week-03-Python\Instructions\PyPoll\raw_data\election_data_1.csv")


row_count = 0
voting_info= []
with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    #next(csv_reader)
    for row in csv_reader:
        voting_info = [[row[0], row[1], row[2]] for row in csv_reader]
        counter = len(list(voting_info)) # Number of votes
        row_count = counter
        print(row_count)


candidate_count = 0
candidate_info = []
with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    #next(csv_reader)
    for row in csv_reader:
        candidate_info = [[row[2]] for row in csv_reader]
        unique_data = [list(row) for row in set(tuple(row) for row in candidate_info)]
        cntr = len(list(unique_data)) # Number of candidates
        candidate_count = cntr
        print(candidate_count)











    




