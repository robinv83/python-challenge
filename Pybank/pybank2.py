import os
import csv

csvpath = os.path.join(r"C:\Users\Admin\Desktop\UNCCHAR201802DATA2-Class-Repository-DATA\Homework\Week-03-Python\Instructions\PyBank\raw_data\budget_data_2.csv")

#Find total number of months

row_count = 0
with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)
    counter = len(list(csv_reader))  
   # print(counter)
    row_count = counter

#Find Total revenue
total_revenue = 0
with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader)
    total_revenue = 0
    for row in csv_reader:
        total_revenue = total_revenue + int(row[1])
   # print(total_revenue)


#Create a list with revenue information
average_rate = 0
with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    #next(csv_reader)
    for row in csv_reader:
        revenue_list = [int(row[1]) for row in csv_reader]
        difference = int(revenue_list[-1] - revenue_list[0])
        average_rate = difference/row_count
       # print(average_rate)

#Greatest increase and decrease in revenue over entire period
fnl_sorted_list = []
with open(csvpath, newline= "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    #next(csv_reader)
    for row in csv_reader:
        str_to_int = [[row[0], int(row[1])] for row in csv_reader]
        sorted_by_second = sorted(str_to_int, key=lambda tup: tup[1])
        fnl_sorted_list = sorted_by_second


print("```")
print("Financial Analysis")
print("---------------------------")
print("")
print("Total Months: " +str(row_count))
print("")
print("Total Revenue: $" + str(total_revenue))
print("")
print("Average Revenue Change: $" + str(round(average_rate, 2)))
print("")
print("Greatest Increase in Revenue: " + str(fnl_sorted_list[-1]))
print("")
print("Greatest Decrease in Revenue: " + str(fnl_sorted_list[0]))




    
        




    





    





#this counts the total rows
#row_count = len(list(csv_reader))   
#print(row_count)

# this sums the total
#for row in csv_reader:
#    total_revenue = total_revenue + int(row[1])
#    print(total_revenue)






