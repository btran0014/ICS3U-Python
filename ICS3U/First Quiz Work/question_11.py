def histogram(alist):
  for i in range(len(alist)):
    asterixes=""
    for x in range(int(alist[i])):
      asterixes+="*"
    print (asterixes)
histogram([4,9,7])
histogram([7,3,9,2])