#  Student Record

student = {}

user_name = input("Kindly enter your name: ")

user_age = int(input("Kindly enter your age: "))


student.update({"name": user_name, "age": user_age})        # Storing the values

scores_list = [70, 90, 80]

student.update({"scores": scores_list})     # Adding the list of scores

average_score = sum(scores_list) / len(scores_list)     # Average score

pass_score = average_score >= 50

student.update({"passed": pass_score})

age_pass = user_age >= 13 and user_age <= 19

student.update({"teenager": age_pass})

print(f"Student record:\nName: {student['name']}\nAge: {student['age']}\nScores: {student['scores']}\nPassed: {student['passed']}\nTeenager: {student['teenager']}")