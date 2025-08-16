#  Task3: Tuple Operations
nigerian_state = (
    input("Enter the first Nigerian state: "),
    input("Enter the second Nigerian state: "),
    input("Enter the third Nigerian state: "),
    input("Enter the forth Nigerian state: "),
    input("Enter the fifth Nigerian state: ")
)
print(f"{nigerian_state[0]} and {nigerian_state[-1]}")
print("Lagos" in nigerian_state)
print("The number of states entered is: ", len(nigerian_state))
