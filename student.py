def add_student():
    """
    Takes the student's name, course grades, and course credits from the user and stores them.
    """
    student_name = input("Enter the student's name: ").strip()
    courses = []
    
    try:
        num_courses = int(input(f"How many courses will you enter for {student_name}?: ").strip())
        
        for i in range(num_courses):
            course_name = input(f"Enter the name of course {i+1}: ").strip()
            try:
                course_grade = float(input(f"Enter the grade for {course_name} (0-100): ").strip())
                if 0 <= course_grade <= 100:
                    course_credit = float(input(f"Enter the credit for {course_name}: ").strip())
                    if course_credit > 0:
                        courses.append((course_grade, course_credit))
                    else:
                        print("Credit must be greater than 0.")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid value entered. Please enter a number.")
        
        if courses:
            return student_name, courses
        else:
            print("No courses added.")
            return None, None
            
    except ValueError:
        print("Invalid number of courses entered.")
        return None, None


def show_students(students):
    """
    Displays the names and courses of students on the screen.
    """
    if len(students) == 0:
        print("No students have been added yet.")
    else:
        for name, courses in students.items():
            print(f"\n{name}:")
            for grade, credit in courses:
                print(f"  - Grade: {grade:.2f}, Credit: {credit}")