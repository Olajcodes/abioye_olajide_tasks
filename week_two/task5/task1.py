# Task1: Create and Display
print("Kindly enter your three favorite Nigerian dishes")
dishes = (input("Enter your favorite dish 1: "),
          input("Enter your favorite dish 2: "),
          input("Enter your favorite dish 3: ")
)
print(dishes)
print(*dishes, sep="\n")