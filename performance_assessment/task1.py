"""
This program is used to tally the votes for different presidential candidates, figure out the percentage of votes per 
candidate and output who the winner is after the voting is finished
"""

#Setting each vote value to 0
candidate_votes = [0,0,0,0]

while True:
    #print all of the presidential candidates and their corresponding numbers then proceeds to ask for votes
    print ("The presidential candidates are: \n 1. Mickey Mouse \n 2. Donald Duck \n 3. Minnie Mouse \n 4. Goofy \n Type 0 to quit.")

    try:
        vote=int(input("Vote?:"))     
    except ValueError:
        print("Please enter a number!")
        break

    if vote == 0:
        break
    elif vote == 1 or vote == 2 or vote == 3 or vote == 4:
        candidate_votes[vote -1] +=1 
    else:
        print ("invalid")
    
total = sum(candidate_votes)
print(f"Here are the votes!{candidate_votes}")

percentage = [0,0,0,0]

for i in range(0,4):
    percentage[i] = round(candidate_votes[i]/total*100)
print (f"Here are the percentages of the votes!:{percentage}")

candidate_votes_index = candidate_votes.index(max(candidate_votes))

#Figures out the winner or if there was a tie
if candidate_votes_index == 0:
    print(f"Mickey Mouse wins!")
    for i in range(0,4):
        if max(candidate_votes) == candidate_votes[i]:
            print("There was a tie!")
elif candidate_votes_index == 1:
    print(f"Donald Duck wins!")
    for i in range(0,4):
        if max(candidate_votes) == candidate_votes[i]:
            print("There was a tie!")
elif candidate_votes_index == 2:
    print(f"Minnie Mouse wins!")
    for i in range(0,4):
        if max(candidate_votes) == candidate_votes[i]:
            print("There was a tie!")
elif candidate_votes_index == 3:
    print(f"Goofy wins!")
    for i in range(0,4):
        if max(candidate_votes) == candidate_votes[i]:
            print("There was a tie!")
