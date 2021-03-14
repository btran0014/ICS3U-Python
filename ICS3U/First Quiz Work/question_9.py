user_int=int(input(("Enter an integer: ")))
original_user_int=user_int
int_sum=0
user_int=list(str(user_int))
for i in range(len(user_int)):
  user_int[i]=int(user_int[i])
print(f"{original_user_int} has: {len(user_int)} digits. The sum of the digits is: {sum(user_int)}.")