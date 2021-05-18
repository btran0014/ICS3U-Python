def histogram(alist):
  for i in range(len(alist)):
    asterixes=""
    for x in range(int(alist[i])):
      asterixes+="#"
    print (asterixes)

list_length = int(input("How long is the list? \n"))
user_list = []

for i in range (list_length):
    num = int(input("How many asterixes? \n"))
    user_list.append(num)    

histogram(user_list)    