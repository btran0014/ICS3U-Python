""" 
This program will do a bunch of tasks after the user inputs a number
"""
import collections
#finds if the number is odd or even
def odd_or_even():  
    if (user_num % 2) > 0: 
            print (user_num, "is an odd number!")
    else:
        print (user_num, "is an even number!")

#finds if the number is prime or not
def prime_or_not():
    if user_num > 1:
        for i in range(2,user_num):
            if (user_num % i) == 0:
                print(user_num,"is not a prime number")
                print(i,"times",user_num//i,"is",user_num)
    print("If nothing is printed, your number is a prime number. Otherwise, the statements above are true.")

#finds the sum of all numbers in list
def sum_of_all_nums():
    sumlist = []
    for i in range (0, user_num+1):
        sumlist.append(i)
    print (f"The sum of all numbers leading up to {user_num} is {sum(sumlist)}")

#finds sum of all digits of input num
def sum_of_all_digits():
    usernumlist = [int(i) for i in str(user_num)]
    print (f"The sum of all digits in {user_num} is {sum(usernumlist)}")

#looks for repeating numbers    
def repeating_nums():
    usernumlist = [int(i) for i in str(user_num)]
    print(f"The repeating digits in the input number are: {[item for item, count in collections.Counter(usernumlist).items() if count > 1]}")
    
            
#main loop for the program and will run all definitions
use_again = input("Would you like to use this program? (Y/N):")
while use_again == "Y":
    user_num = 1
    while user_num != -1: 
        try:
            print("Enter a number between 0 and 999999999.\n Enter -1 to exit")
            user_num = int(input("What is your number?: "))
            odd_or_even()
            prime_or_not()
            sum_of_all_nums()
            sum_of_all_digits()
            repeating_nums()
        except ValueError:
            print("You must enter a number!")
        use_again = input("Would you like to use this program again? (Y/N):")
print("Thanks for using the program!")