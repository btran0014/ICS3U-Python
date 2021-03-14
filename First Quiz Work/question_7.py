print ("Please type 'quit' if you would like to stop")
count=0
while True:
  user_inp=input("Enter a WORD:")
  if user_inp!= "quit":
    count+=1
  else:
    break
print (f"You entered {count} words")

""" 
since the program adds 1 to count each time it sees that user_inp does not equal quit, it will add 1 regardless of what is entered.
Therefore, any string that is added will only count as 1 word.
"""