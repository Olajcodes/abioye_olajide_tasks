# # Ask user for their name
# name = input("Enter your name: ") 

# # Ask for their age
# age = int(input("Enter your age: "))

# # Ask the user for their test core
# score = int(input("Enter your test score: "))

# # Check age eligibility
# eligibility = (age < 18) and (score > 70)

# # printing out the details using escape sequence
# print(f"Candidate: {name}\nage: {age}\nScore: {score}\nEligible: {eligibility}")

'''
The code is taking input from user from asking their name, age and test score to check their eligibility.
checking if user's age is below 18 and their scoe is above 70.
It also prints out their details using f-strings and escape sequence.
'''

# Federal Government Scholarship Key eligibility Requirements
name = input("Enter your name: ")

citizenship = input("Are you a Nigerian?: ").title()

enrollment = input("Are you currently a full-time undergraduate student in Nigeria? (Yes/No): ").title()

other_scholarships = input("Are you currently on any scholarship related to Oil and Gas industry? (Yes/No): ").title()

academic_qualification = input("Do you have five distinctions (A's and B's) in relevant subsets in WASSCE (may/June) exams, including English and Mathematics? (Yes/No): ").title()

eligibility = ((citizenship == "Yes") and (enrollment == "Yes") and (other_scholarships == "No") and (academic_qualification == "Yes"))

print(f"The eligibility status for {name} is {eligibility}")