use_again = "Y"

#loop for using program again
while use_again == "Y": 
  while True: 
    try:
      eq_type = int(input("What equation would you like to use? \n1 for linear. \n2 for quadratic.\nYour choice: "))
      if eq_type != 1 and eq_type != 2:
        print("Invalid input! Please enter either a 1 or a 2.")
      else:
        break
    except ValueError:
      print("Invalid input! You must enter an integer.")

  #determining the equation type and how to continue    
  if eq_type == 1:
    print("You chose linear.")
  elif eq_type == 2:
    print("You chose quadratic.")
  else:
    print("Please enter either 1 or 2.")

  #ask for the 3 inputs for equation
  while True:
    try:
      a_inp = int(input("What is the a value?: "))
      b_inp = int(input("What is the b value?: "))
      c_inp = int(input("What is the c value?: "))
      break
    except ValueError:
      print("Invalid input! You must enter a number.")

  #linear equation calculations and prints table
  if eq_type == 1:
    print(f"{'':<5} X values:{'':<10} Y values:")
    for x in range (-4,5):
      y = (a_inp * x + c_inp)/-b_inp
      if abs(y) == 0:
        y = 0.0
      if x <0:
        print (f"{'':6.1} {float(x)},end=''")
      else:
        print (f"{'':7.1} {float(x)},end=''")
      #prevents the printing of -0.0
      if y <0:
        print (f"{'':16.1} {y}")
      else:
        print (f"{'':17.1} {y}")
  #quadratic equation calculations
  if eq_type ==2:
    print(f"{'':<5} x values:{'':<10} {y} values:")
    for x in range (-4,5):
      y = (a_inp*x**2 + b_inp*x + c_inp)
      print(y)