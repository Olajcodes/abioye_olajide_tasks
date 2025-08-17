#  Days and Activities Pairing

days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

activities = (input("Enter the activity for Sunday:  "), input("Enter the activity for Monday:  "), input("Enter the activity for Tuesday:  "))

pair_dict = {day: activity for day, activity in zip(days_of_week, activities)}

print(pair_dict)