# Unique Members Registration

user_name = input("Kindly enter three names separated by comma: ")

set_user_name = set(user_name.split(","))

names_dict = {name: len(name) for name in set_user_name}

print(names_dict)