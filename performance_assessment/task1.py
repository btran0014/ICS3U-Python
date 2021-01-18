while True:
    print ()
    print ("The presidential candidates are:")
    print ("1. Mickey Mouse")
    print ("2. Donald Duck")
    print ("3. Minnie Mouse")
    print ("4. Goofy")
    print ("Type 0 to quit")
    v=int(input("Vote? "))
    if v==3:
        N+=1
    if v == 0:
        break
    if v==2:
        D+=1
    if v==1:
        M+=1
    if v==4:
        G+=1
    else:
        print ("invalid")
        continue

T=M+D+N+G
print (T)
if M>D and M>N and M>G:
    print("Mickey Mouse wins!")
    print (M/T*100,"% of the votes")
elif D>N and D>G and D>M:
    print ("Donald Duck wins!")
    print (D/T*100,"% of the votes")
elif N>G and N>M and N>D:
    print("Minnie Mouse wins!")
    print (N/T*100,"% of the votes")
elif G>M and G>N and G>D:
    print("Goofy wins!")
    print (G/T*100,"% of the votes")


