#   Unique Name Collector
'''
- Accept names of people
- No duplicates allowed (Use set to get input, then convert to list so i can sort)
- Display in alphabetic order
'''

names_attending_seminar = {input("Enter your name: "), input("Enter your name: "), input("Enter your name: "), input("Enter your name: "), input("Enter your name: ")}

order_names_attending_seminar = list(names_attending_seminar)

print(sorted(order_names_attending_seminar))