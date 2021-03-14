
"""
a) the output does not change depending on the code version.
b)Version 3 is the most efficient and easiest to understand. Version 2 checks for multiple conditions using AND comparisons whereas version 3 completes the same task using only
one condition per if statement. Version 1 doesn't use elif statements but uses else and if seperately instead.
"""
user_purchase=float(input("What is the total of your purchase?: "))
if user_purchase<=0.0:
  print ("Invalid Price ")
elif user_purchase>=100:
  print (f"You are eligible for 40% off in savings\nHere is your new total! {user_purchase - user_purchase*0.4}")
elif user_purchase>=75:
  print (f"You are eligible for 30% off in savings\nHere is your new total! {user_purchase - user_purchase*0.3}")
elif user_purchase>=50:
  print (f"You are eligible for 20% off in savings\nHere is your new total! {user_purchase - user_purchase*0.2}")
elif user_purchase>=25:
  print (f"You are eligible for 10% off in savings\nHere is your new total! {user_purchase - user_purchase*0.1}")
else:
  print ("You are not eligible for savings")