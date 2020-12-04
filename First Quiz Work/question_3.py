while True:
  user_inp=float(input("What is your mark?: "))
  if  user_inp>=0 and  user_inp<=100:
    break
  else:
    print("Invalid Mark")
print("Thank You!")