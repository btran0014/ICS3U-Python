

if account_balance > 0:

  if withdraw <= account_balance:
    print("Transaction is accepted")


  elif withdraw <= (account_balance + OVERDRAFT):
    print("The account is overdrawn")


  elif withdraw > (account_balance + OVERDRAFT):
    print("Transaction is refused")

  print("Your account balance is: $", new_balance)

else:
  print("Please enter a positive integer")
  exit()

#Constants:
OVERDRAFT = 50

#inputs
account_balance = float(input("What is the opening balance? "))
withdraw = float(input("How much would you like to take out? "))

#variables
new_balance = account_balance - withdraw