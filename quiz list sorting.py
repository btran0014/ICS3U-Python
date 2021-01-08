def sortList(list):
    newlist =[]
    for i in range(len(myList)):
        min_index = myList.index(min(myList))
        newlist.append(myList.pop(min_index))   
    return newlist

user_inp = float(input("Enter a number to store: "))
myList = []
myList.append(user_inp)

while user_inp !=-1:
    print ("Enter -1 to quit")
    try:
        user_inp = float(input("Enter a number to store: "))
        if user_inp==-1:
            continue
        else:
            myList.append(user_inp)
    except ValueError:
        print("Please Enter a number!")

print(myList)
print(sortList(myList))