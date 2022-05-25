student_scores = {
    "Harry":81,
    "Ron": 78,
    "Hermonie":99,
    "Draco":74,
    "Neville":62,
}

# Empty dictionaryn to keep track of grades
student_grades ={}

# Loop through dictionary
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key]= "Outstanding"

    elif student_scores[key] >= 81 or student_scores[key] ==90:
        student_grades[key]="Exceeds Expectations"    

    elif student_scores[key] >= 71 or student_scores[key] ==80:
        student_grades[key]="Acceptable"    
        
    elif student_scores[key] < 70:
        student_grades[key]="Fail"    

print(student_grades)