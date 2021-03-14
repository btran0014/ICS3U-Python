amount = int(input("How many numbers?: "))
num_list = []
sum_of_nums = 0

for i in range(amount):
    number = int(input("What is your number?: "))
    num_list.append(number) 
    sum_of_nums += number

print(f"This is your sorted list: {sorted(num_list)}.\nTHe sum of all values in the list is {sum_of_nums}.")