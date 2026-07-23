
print("===== Student Record Management System =====")
students = []
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
       
        student = {

           "Name": name,
            "Age": age,
           "Course": course
        }

        students.append(student)
        print("Student Added Successfully!")
    
    elif choice == "2":
    
        if len(students) == 0:
            print("No Students Found!")

        else:
            for student in students:   
                print("----------------------")
                print("Name :", student["Name"])
                print("Age :", student["Age"])
                print("Course :", student["Course"])
    elif choice =="3":
        name = input("Enter Student Name: ")

        if len(students) == 0:
            print("No Students Found!")
        else:
            found = False

            for student in students:   
                if student["Name"]== name:
                    print("student found..!")
                    print("Name :", student["Name"])
                    print("Age :", student["Age"])
                    print("Course :", student["Course"])
                    found = True
                    break
            if found == False:
               print("student not found")
    elif choice == "4":
        name = input("Enter Student Name to Update: ")

        found = False

        for student in students:
            if student["Name"] == name:
                print("Student Found!")

                age = input("Enter New Age: ")
                course = input("Enter New Course: ")

                student["Age"] = age
                student["Course"] = course

                print("Student Updated Successfully!")

                found = True
                break

        if found == False:
               print("Student Not Found!")


    elif choice == "5":
                name = input("Enter Student Name to Update: ")

                found = False
                for student in students:
                    if student["Name"] == name:
                     students.remove(student)
                     print("Student Deleted Successfully!")

                     found = True
                if found == False:
                    print("student not found..!")