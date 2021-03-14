"""
this program is a grade checker when names, numbers and grades are entered in lists

"""
student_names = ["Anouk", "Emily", "Luka", "Chris", "Joel", "Thea", "Jeremie"]
student_no = [902020, 663728, 783939, 978253, 662784, 562721, 652367]
grades = [87, 67, 71, 97, 78, 53, 31]

passed = []
passed_no = []

index = 0

for i in range (len(grades)):
    num_index = student_no[index]
    name_index = student_names[index]
    
    if 60 <= grades[index]:
        print (name_index, num_index)
    index +=1