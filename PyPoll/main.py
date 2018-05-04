#Modules
import os
import csv

#I/O path
csvpath = os.path.join('.', 'raw_data', 'election_data_1.csv')
writepath=os.path.join('.','election_result_1.csv')

#open raw data 
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    next(csvreader)
    
    #initiate variables/lists 
    CandiCount=0

    #get the first row to create the lists for candidates and votes
    firstline=next(csvreader)
    CandiList=[firstline[2]]              #list for candidates     
    CandiVote=[1]                         #votes for respective cadidates
    total_vote=1


    for row in csvreader:
        #count total votes
        total_vote+=1  
        #get the candidate
        Candidate=row[2]         
                
        
        i=0
        while i < len(CandiList):                #compare the candidate with the list
            if Candidate == CandiList[i]:        #if the candidate matches the name in the list   
                CandiVote[i]=CandiVote[i]+1      #add a vote to the candidate 
                break                            #stop comparing
            else:
                i=i+1                            #if not match, compare to the next in the list 

        if i == len(CandiList):                  #If none was matched 
            CandiList.append(Candidate)          #add this new candidate to the list
            CandiVote.append(1)                  #add the first vote     
    
    #get the winner 
    Winner=CandiList[CandiVote.index(max(CandiVote))]

    print("Election Results")
    print("-----------------------")    
    print("Total votes:",total_vote)
    print("-----------------------")
    for x in range(len(CandiList)):
        VotePercentage=float(CandiVote[x]/total_vote)
        print(CandiList[x],":",'{0:0.1%}'.format(VotePercentage),"(",CandiVote[x],")")
    print("-----------------------")
    print("Winner: ",Winner)
            
#output to file
with open(writepath,'w',newline='') as csvfile:
    csvfile.write("Election Results\n")
    csvfile.write("-----------------------\n")    
    csvfile.write("Total votes: "+str(total_vote)+"\n")
    csvfile.write("-----------------------\n")
    for x in range(len(CandiList)):
        Candidate=CandiList[x]
        VotePercentage='{0:0.1%}'.format(float(CandiVote[x]/total_vote))
        Votes=CandiVote[x]
        csvfile.write(Candidate+": "+VotePercentage+"("+str(Votes)+")\n")
    csvfile.write("-----------------------\n")
    csvfile.write("Winner: "+Winner)

   


