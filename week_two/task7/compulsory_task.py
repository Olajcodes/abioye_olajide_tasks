#  Student Profile Builder

name = input("Enter your name: ")
age = int(input("Kindly provide your age: "))
gender = input("Provide your gender: ")

courses = ("Phs", "Chm", "Bio", "Mts")
scores = tuple(float(input(f"Kindly enter the score for {course}: ")) for course in courses)

guardian_name = input()