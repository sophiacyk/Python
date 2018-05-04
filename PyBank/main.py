#Modules 
import os
import csv

#import the dataset from files 
csvpath = os.path.join('.', 'raw_data', 'budget_data_1.csv')
writepath=os.path.join('budget_data_describe_1.csv')

print(csvpath)

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip header
 

    #initiate variables 
    monthCount=0
    revenue=0
    revPrevious=0

    MaxRevenue=0
    MinRevenue=0

    Total_change=0


    for row in csvreader: 
        
        #count total month and revenue 
        monthCount=monthCount+1
        revenue=revenue+float(row[1])
        
        #start from the 2nd month to calculate change and get min and max
        if monthCount>1:   
            change = float(row[1])-revPrevious
            Total_change=Total_change+change
            #when the revenue is positive, look for the greatest increase
            if change>MaxRevenue:
                MaxRevenue=change
                MaxMonth=row[0]
            #when the revenue is negative, look for the greatest decrease
            if MinRevenue>change:
                MinRevenue=change
                MinMonth=row[0]
        
        #store the revenue for next month to compare
        revPrevious=float(row[1])  
    
    #get the average revenue
    Average_revenue_change=float(Total_change/(monthCount-1))
    
    #output to the display
    print("Finacial Analysis")
    print("-----------------------")
    print("Total Months:",monthCount)
    print("Total Revenue: $",revenue)
    print("Average Revenue Change: $",Average_revenue_change)
    print("Greatest Increase in Revenue: ",MaxMonth,"($",MaxRevenue,")")
    print("Greatest Decrease in Revenue: ",MinMonth,"($",MinRevenue,")")

#  Open the output file
with open(writepath,'w',newline='') as csvfile:

    #output to the file
    csvfile.write("Finacial Analysis\n")
    csvfile.write("-----------------------\n")
    csvfile.write("Total Months: ")
    csvfile.write(str(monthCount)+"\n")
    csvfile.write("Total Revenue: ")
    csvfile.write("$"+str(revenue)+"\n")
    csvfile.write("Average Revenue Change: $"+'{0:.2f}'.format(Average_revenue_change)+"\n")
    csvfile.write("Greatest Increase in Revenue: "+str(MaxMonth)+"($"+str(MaxRevenue)+")\n")
    csvfile.write("Greatest Decrease in Revenue: "+str(MinMonth)+"($"+str(MinRevenue)+")")

    





