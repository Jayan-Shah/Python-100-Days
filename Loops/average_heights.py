student_heights = input("Input a list of student heights: ").split(",")

totalheight = 0
for height in student_heights:
    totalheight = int(height) + totalheight

print(f"Average height of all students are {totalheight/len(student_heights)}")

#  To get len using for
numberofStudents=0
for student in student_heights:
    numberofStudents+=1
print(numberofStudents)

# To get the largest height not using sum() function
tallest=0
for student in student_heights:
    if int(student)>tallest:
        tallest=int(student)

print(tallest)
