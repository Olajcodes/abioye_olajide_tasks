#  Student Profile Builder

# Collecting personal details
name = input("Enter your name: ")
age = int(input("Kindly provide your age: "))
gender = input("Provide your gender: ")

# Getting the guardian's details
guardian_name = input("Kindly enter the guardian's name: ")
guardian_phone = input("Kindly enter your phone number: ")

# Getting academic details
courses = ("Phs", "Chm", "Bio", "Mts")
scores = tuple(float(input(f"Kindly enter the score for {course}: ")) for course in courses)

# Hobbies - getting it in a set to ensure uniqueness.
hobbies = input("Enter your hobbies (with comma separated): ")
hobbies_set = set(hobby.strip for hobby in hobbies.split(","))

# Setting up the student's profile
student_profile = {
    "Basic Info": {
        "Name": name.title(),
        "Age": age,
        "Gender": gender.upper()
    },
    "Academics Info": {course: score for course, score in zip(courses, scores)},
    "Guardian Info": {
        "Name": guardian_name.title(),
        "Phone": guardian_phone
    },
    "Hobbies": list(hobbies_set)
}

# Calculated data
student_profile["Academics Info"]["Average"] = sum(scores) / len(scores)
student_profile["Basic Info"]["Initials"] = "".join([n[0] for n in name.split()])
student_profile["Hobbies Count"] = len(hobbies_set)

# Displaying the results
print("\n\t=== STUDENT PROFILE ===")
print(f"Name:\t\t{student_profile['Basic Info']['Name']}")
print(f"Age:\t\t{student_profile['Basic Info']['Age']}")
print(f"Gender:\t\t{student_profile['Basic Info']['Gender']}")
print(f"Initials:\t{student_profile['Basic Info']['Initials']}")
print("\n--- Academic Scores ---")
print(student_profile["Academics Info"])
print("\n--- Guardian Info ---")
print(student_profile["Guardian Info"])
print("\n--- Hobbies ---")
print(student_profile["Hobbies"])
print(f"\nTotal Hobbies:\t{student_profile['Hobbies Count']}")
print(f"Average Score:\t{student_profile['Academics Info']['Average']:.2f}")