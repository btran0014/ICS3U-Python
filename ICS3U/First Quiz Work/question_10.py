import random
while True:
  rand_int = int(random.randrange(1,7,1))
  new_roll =-1
  count = 0
  print (f"Your first roll and point value is: {rand_int}")
  while new_roll != rand_int:
    new_roll=random.randrange(1,7,1)
    print (f"Next roll is: {new_roll}")
    count+=1
  print (f"It took you {count} times to get your point again.")
  play_again=input("Do you want to play again(Y/N) ")
  if play_again == "Y":
    continue
  else:
    break