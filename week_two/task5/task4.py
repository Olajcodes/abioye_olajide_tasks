#  Task4: Tuple Unpacking
user_profile = (
    input("Enter your first name: "),
    int(input("Enter your age: ")),
    input("Enter your favorite color: "),
    input("Enter your home town: ")
)

first_name, age, favourite_color, home_town = user_profile      # Unpacking

print(f"Below is the {first_name}\'s profile:\nFirst Name:\t{first_name}\nAge:\t\t{age}\nColor:\t\t{favourite_color}\nHome town:\t{home_town}")
