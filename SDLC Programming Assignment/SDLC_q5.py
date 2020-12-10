import random
#creates variable that decides if the game will continue
play_again = "Y"
#initial game loop
while play_again == "Y":
    #ask for gamemode type
    while True: 
        try:
            method = int(input("Which mode do you want to play? Enter 1 for default. Enter 2 for custom.: ")) 
            if method != 1 and method !=2:
                print("Invalid input! Please enter either a 1 or a 2.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter either a 1 or a 2.")

    count = 0
    #default gamemode (1-100) if method is 1. Custom if 2. invalid if anything greater than 2.
    if method == 1:
        min_val, max_val = 0, 100
    
    elif method == 2:
        while True:
            try:
                min_val = int(input("Enter the minimum value: "))
                if min_val >=0:
                    max_val = int(input("Enter the maximum value: "))
                    if max_val > min_val:
                        break
                    else:
                        print("Invalid input! The maximum number must be greater than the minimum number.")
                else:
                    print("Invalid input! The number cannot be negative.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    #stores a random number between user input max and min values
    rand_val = random.randrange(min_val, max_val + 1) 
    guess = int

    #user guesses the number until it is right
    while guess != rand_val:
        while True:
            try:
                guess = int(input("What is your guess?: "))
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")
        #keeps track of guesses
        count += 1
        #outputs for guesses depending on the input
        if guess < min_val or guess > max_val:
            print (f" Invalid input! Enter a number within the range of values of {min_val} and {max_val}.")
        elif guess > rand_val:
            print("Too high! Try again!")
        elif guess < rand_val:
            print("Too low! Try again!")
    print (f"Congratulations. It took you {count} tries to correctly guess the number.")

    #ask if user plays again
    while True:
        play_again = input("Would you like to play again? (Y/N)")
        if play_again == "Y" or play_again == "N":
            break
        else:
            print("Please enter: Y or N.")
            continue