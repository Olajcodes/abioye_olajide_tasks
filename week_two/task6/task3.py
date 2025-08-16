#  Simulate a football match ticket system
'''
- Store all seat numbers (1 to 50) in a set (more of hardcoding)
- Ask users for input in "int" to "book" a seat (Use 3 users)
- removed booked seats from the set
- print the remaining seats after booking
'''

seat_number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}

user_booked_seat_1 = int(input("Kindly book a seat by choosing (1 - 50): "))
seat_number.discard(user_booked_seat_1)
print(f"The remaining seats after you booked is {seat_number}")

user_booked_seat_2 = int(input("Kindly book a seat by choosing (1 - 50): "))
seat_number.discard(user_booked_seat_2)
print(f"The remaining seats after you booked is {seat_number}")

user_booked_seat_3 = int(input("Kindly book a seat by choosing (1 - 50): "))
seat_number.discard(user_booked_seat_3)
print(f"The remaining seats after you booked is: {seat_number}")