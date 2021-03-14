start_val=int(input("Enter the starting value: "))
end_val=int(input("Enter the ending value: "))
increment=int(input("What is the increment?: "))

print(f"{'List Value':>13}{'Square':>13}")

for i in range(start_val,end_val+1,increment):
  print(f"{i:>13}{i**2:>13}")