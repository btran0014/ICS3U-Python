#linear calculations
def linear():
    print(f"{'':<5} X values:{'':<10} Y values:")
    for x in range (-4,5):
      y = (a_inp * x + c_inp)/-b_inp
      if abs(y) == 0:
        y = 0.0
      if x <0:
        print (f"{round(float(x),1):11}", end='')
      else:
        print (f"{round(float(x),1):11}", end='')
      #prevents the printing of -0.0
      if y <0:
        print (f"{round(y,1):19}")
      else:
        print (f"{round(y,1):19}")
#quadratic calculations
def quadratic():
    print(f"{'':5} x values:{'':10} Y values:")
        #coord of x vertex
    x_vertex = b_inp/(2*a_inp)-6
        
    for i in range(11):
        x_vertex += 1
        #coord of y vertex
        y_vertex = ((a_inp*x_vertex**2) + (b_inp * x_vertex) + c_inp)
        print(f"{round(x_vertex,1):12} {round(y_vertex,2):18}")
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

  if eq_type == 1:
    linear()
    while True: 
        use_again = input("Would you like to use this program again? (Y/N)")
        if use_again == "Y":
            break
        elif use_again != "Y" and use_again != "N":
            print("Please enter: Y or N.")
        print("Thanks for using this program!")
        break
  if eq_type ==2:
    quadratic()

    while True: 
        use_again = input("Would you like to use this program again? (Y/N)")
        if use_again == "Y":
            break
        elif use_again != "Y" and use_again != "N":
            print("Please enter: Y or N.")
        print("Thanks for using this program!")
        break
        