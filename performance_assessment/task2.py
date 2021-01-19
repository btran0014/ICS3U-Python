def odd_or_even():
    if (user_num % 2) > 0: 
            print (user_num, "is an odd number!")
    else:
        print (user_num, "is an even number!")

def prime_or_not():
    prime = True
    for i in range (2, user_num//2):
        prime == True
        if (user_num % i)==0:
            prime == False 
            break
        elif prime == False: 
            print(user_num, "is not a prime number.")
            break
        elif prime == True:
            print (user_num, "is a prime number")

    
    




use_again = input("Would you like to use this program? (Y/N).")
while use_again == "Y":
    user_num = 1
    while user_num != -1: 
        try:
            print("Enter a number between 0 and 999999999.\n Enter -1 to exit")
            user_num = int(input("What is your number?: "))
            odd_or_even()
            prime_or_not()

        except ValueError:
            print("You must enter a number!")
        use_again = input("Would you like to use this program again? (Y/N).")
print("Thanks for using the program!")