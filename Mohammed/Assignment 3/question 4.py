def compute_avg_grade(department, course_number):
    grades = []
    with open('Mohammed\\Assignment 3\\grades.txt', 'r') as file:
        for line in file:
            fields = line.strip().split()
            if fields[0] == department and fields[1] == course_number:
                grades.append(int(fields[3]))
    average = sum(grades) / len(grades)
    return "{:.2f}".format(average)
    
def compute_gpa(student_number):
    grades = []
    with open('Mohammed\\Assignment 3\\grades.txt', 'r') as file:
        for line in file:
            fields = line.strip().split()
            if fields[2] == student_number:
                grades.append(int(fields[3]))
    gpa = sum(grades) / len(grades)
    return "{:.2f}".format(gpa)

def failed_students(department, course_number):
    count = 0
    with open('Mohammed\\Assignment 3\\grades.txt', 'r') as file:
        for line in file:
            fields = line.strip().split()
            if fields[0] == department and fields[1] == course_number and int(fields[3]) < 75:
                count += 1
    return count

def iGrade():
    print('im running\n')
    while True:
        choice = input()
        if choice == 'quit':
            break
        elif choice.startswith('avg'):
            department, course_number = choice.split()[1:]
            avg = compute_avg_grade(department, course_number)
            print(avg)
        elif choice.startswith('gpa'):
            student_number = choice.split()[1]
            gpa = compute_gpa(student_number)
            print(gpa)
        elif choice.startswith('fails'):
            department, course_number = choice.split()[1:] 
            count = failed_students(department, course_number)
            print(count)

iGrade()