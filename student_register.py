# Open file
with open("reg_form.txt", "w", encoding = "utf-8") as file:

    # Create variable asking user to input number of entries
    number_of_students = int(input("\nHow many students do you want to register?\n"))

    # Iterate through the number of students
    for num in range(number_of_students):
        
        # User input the student ID number
        student_id = input("Please enter student ID number\n")

        # write the above input to a text file with dotted lines for signature
        file.write(f'Student {student_id}:    .................\n')

