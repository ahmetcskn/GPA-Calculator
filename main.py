from student import add_student, show_students
from calculation import calculate_weighted_average

def main():
    students = {}

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("1 - Add New Student")
    print("2 - View Existing Students")
    print("3 - Calculate Average")
    print("4 - Exit")

    while True:
        try:
            choice = int(input("\nChoose an option (1-4): ").strip())

            if choice == 1:
                name, courses = add_student()
                if name and courses is not None:
                    students[name] = courses
                else:
                    print("Student not added. Invalid course or name.")

            elif choice == 2:
                print("\nExisting Students and Courses:")
                show_students(students)

            elif choice == 3:
                if students:
                    for name, courses in students.items():
                        average = calculate_weighted_average(courses)
                        print(f"{name}'s weighted average: {average:.2f}")
                else:
                    print("You haven't added any students yet. Please add students first.")

            elif choice == 4:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please choose between 1-4.")
        except ValueError:
            print("Please enter a valid number.")


# Run the program
if __name__ == "__main__":
    main()