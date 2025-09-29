#  TASK FIVE: Student Score Tracker
student_names = []
student_score = []

student_names_request_1 = input("What is the student\'s name: ")
student_names.append(student_names_request_1)
student_score_request_1 = int(input("What is the corresponding Score?: "))
student_score.append(student_score_request_1)

student_names_request_2 = input("What is the student\'s name: ")
student_names.append(student_names_request_2)
student_score_request_2 = int(input("What is the corresponding Score?: "))
student_score.append(student_score_request_2)

student_names_request_3 = input("What is the student\'s name: ")
student_names.append(student_names_request_3)
student_score_request_3 = int(input("What is the corresponding Score?: "))
student_score.append(student_score_request_3)

print("The formatted score sheet is below: ")
for i in range(3):
    print(f"{student_names[i]}:\t{student_score[i]}")