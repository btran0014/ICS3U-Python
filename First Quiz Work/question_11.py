def histogram(alist):
  for i in range(len(alist)):
    asterixes=""
    for x in range(int(alist[i])):
      asterixes+="*"
    print (asterixes)
histogram([5,9,7])