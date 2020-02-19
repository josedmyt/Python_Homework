import os
import csv
import statistics

vote_path= os.path.join("C:/Users/josed/Desktop/UT-TOR-DATA-PT-01-2020-U-C/03-Python/Instructions/PyPoll/Resources/election_data.csv")

voterid=[]
counties=[]
candidates=[]
can1=0
can2=0
can3=0
can4=0
list_candidates=[]

with open(vote_path,newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header=next(reader)
    for row in reader:
        voterid.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
        
    set_candidates= sorted(set(candidates))
    for c in set_candidates:
        list_candidates.append(c)
 
    for item in candidates:
        if item==list_candidates[0]:
            can1 = can1 + 1
        elif item==list_candidates[1]:
            can2 = can2 + 1
        elif item==list_candidates[2]:
            can3 = can3 + 1
        if item==list_candidates[3]:
            can4 = can4 + 1

    total_votes= len(voterid)
    can1p=round((can1/total_votes)*100,3)
    can2p=round((can2/total_votes)*100,3)
    can3p=round((can3/total_votes)*100,3)
    can4p=round((can4/total_votes)*100,3)
    winner = list_candidates[1]

    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    print(f"{list_candidates[1]}: {can2p}% ({can2})")
    print(f"{list_candidates[0]}: {can1p}% ({can1})")
    print(f"{list_candidates[2]}: {can3p}% ({can3})")
    print(f"{list_candidates[3]}: {can4p}% ({can4})")
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

outpath= "Desktop/Homework/Python_Homework/PyPoll/Results.txt"

with open(outpath,'w',newline='') as text:
    print("Election Results", file=text)
    print("--------------------------",file=text)
    print(f"Total Votes: {total_votes}", file=text)
    print("--------------------------",file=text)
    print(f"{list_candidates[1]}: {can2p}% ({can2})", file=text)
    print(f"{list_candidates[0]}: {can1p}% ({can1})", file=text)
    print(f"{list_candidates[2]}: {can3p}% ({can3})", file=text)
    print(f"{list_candidates[3]}: {can4p}% ({can4})", file=text)
    print("--------------------------",file=text)
    print(f"Winner: {winner}",file=text)
    print("--------------------------",file=text)
