import os
import csv
import pandas as pd

csvpath = os.path.join(r"C:\Users\Admin\Desktop\UNCCHAR201802DATA2-Class-Repository-DATA\Homework\Week-03-Python\Instructions\PyBank\raw_data\budget_data_1.csv")

#Find total number of months

with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)
    row_count = len(list(csv_reader))  
    print(row_count)

#Find Total revenue

with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)
    total_revenue = 0
    for row in csv_reader:
        total_revenue = total_revenue + int(row[1])
    print(total_revenue)


#Create a list with revenue information

with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    #next(csv_reader)
    for row in csv_reader:
        revenue_list = [int(row[1]) for row in csv_reader]
        print(revenue_list)
        difference = int(revenue_list[-1] - revenue_list[0])
        print(difference)
row_count = len(list(csv_reader))
print(row_count)


    
        




    





    





#this counts the total rows
#row_count = len(list(csv_reader))   
#print(row_count)

# this sums the total
#for row in csv_reader:
#    total_revenue = total_revenue + int(row[1])
#    print(total_revenue)






