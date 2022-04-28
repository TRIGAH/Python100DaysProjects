student_heights = input("Enter a list of Students Heights seperated by a space: ").split()
sum = 0
num_students = 0

for n in student_heights:
    sum += int(n)
    num_students+=1

average_height = round(sum /num_students)

print(f"The Average height of the students is {average_height}")