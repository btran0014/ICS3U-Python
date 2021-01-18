"""
This program is used to tally the votes for different presidential candidates, figure out the percentage of votes per 
candidate and output who the winner is after the voting is finished
"""
#Setting each vote value to 0
minnie_votes = 0
donald_votes = 0
mickey_votes= 0
goofy_votes = 0

while True:
    #print all of the presidential candidates and their corresponding numbers then proceeds to ask for votes
    print ("The presidential candidates are: \n 1. Mickey Mouse \n 2. Donald Duck \n 3. Minnie Mouse \n 4. Goofy \n Type 0 to quit.")
    vote=int(input("Vote?:"))

    # tallies up the votes as they are being entered
    if vote == 1:
        mickey_votes += 1
    
    elif vote == 2:
        donald_votes += 1
    
    elif vote == 3:
        minnie_votes += 1

    elif vote == 4:
        goofy_votes += 1

    elif vote == 0:
        break

    else:
        print ("invalid")
        continue

    #total votes
    total_votes = mickey_votes + donald_votes + minnie_votes + goofy_votes
    print (total_votes)

#determines the winner and their percentage of the total votes
if mickey_votes > donald_votes and mickey_votes > minnie_votes and mickey_votes > goofy_votes:
    print("Mickey Mouse wins!")
    print (mickey_votes/total_votes * 100,"% of the votes")

elif donald_votes > minnie_votes and donald_votes > goofy_votes and donald_votes > mickey_votes:
    print ("Donald Duck wins!")
    print (donald_votes/total_votes * 100, "% of the votes")

elif minnie_votes > goofy_votes and minnie_votes > mickey_votes and minnie_votes > donald_votes:
    print("Minnie Mouse wins!")
    print (minnie_votes/total_votes * 100, "% of the votes")

elif goofy_votes > mickey_votes and goofy_votes > minnie_votes and goofy_votes > donald_votes:
    print("Goofy wins!")
    print (goofy_votes/total_votes * 100, "% of the votes")

else:
    print("There was a tie!")