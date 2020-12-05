start_val=int(input("Enter the starting value: "))
end_val=int(input("Enter the ending value: "))
increment=int(input("What is the increment?: "))
print("{:>13}{:>13}".format("List Value","Square"))
for i in range(start_val,end_val+1,increment):
  print("{:>6}{:>20}".format(i,i**2))