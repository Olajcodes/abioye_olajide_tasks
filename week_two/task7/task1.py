#  Student Bio Data Storage

student_courses = []
student_name = input("Kindly enter your name: ")
student_age = int(input("What's your age?:"))
student_gender = input("Are you a Male or Female?: ")
student_courses.append(input("Kindly enter your course: "))

student_bio_data = {
    "name": student_name,
    "age": student_age,
    "gender": student_gender,
    "courses": student_courses
}

print(f"The Bio-data for student {student_name} is:\nName: \t\t{student_bio_data['name']}\nAge: \t\t{student_bio_data['age']}\nGender: \t{student_bio_data['gender']}\nCourses: \t{student_bio_data['courses']}")

