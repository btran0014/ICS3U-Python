mark = float(input("Enter your test mark: "))

#"""

print ("Version 1")
if mark > 84 and mark <=100:
    print ("Level 4")
else:
    if mark >=70 and mark <85:
        print ("Level 3")
    else:
        if mark >=60 and mark <70:
            print ("Level 2")
        else:
            if mark >=50 and mark <60:
                print ("Level 1")
            else:
                if mark >=0 and mark<50:
                    print ("Level R")
                else:
                    print ("Mark not in range")

#"""

print ("Version 2")
#Version 2 of marks
if mark > 84 and mark <=100:
    print ("Level 4")
elif mark >=70 and mark <85:
    print ("Level 3")
elif mark >=60 and mark <70:
    print ("Level 2")
elif mark >=50 and mark <60:
    print ("Level 1")
elif mark >=0 and mark<50:
    print ("Level R")
else:
    print ("Mark not in range")

print ("Version 3")
#Version 3 of marks
if mark > 100 or mark < 0:
    print ("Mark not in range")
elif mark >84:
    print ("Level 4")
elif mark >=70:
    print ("Level 3")
elif mark >=60:
    print ("Level 2")
elif mark >=50:
    print ("Level 1")
else:
    print ("Level R")

print ("Thank you and goodbye")

"""
a) the output does not change depending on the code version.
b)Version 3 is the most efficient and easiest to understand. Version 2 checks for multiple conditions using AND comparisons whereas version 3 completes the same task using only
one condition per if statement. Version 1 doesn't use elif statements but uses else and if seperately instead.
"""