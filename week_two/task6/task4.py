#  Creating unique voters registration system

voter_names = set()
voter_1 = input("Kindly enter your name: ")
voter_names.add(voter_1)

voter_2 = input("Kindly enter your name: ")
voter_names.add(voter_2)
# name = voter_1
if voter_1 == voter_2 in voter_names:
    print(f"{voter_1} is trying to register twice and it is not allowed")

voter_3 = input("Kindly enter your name: ")
voter_names.add(voter_3)
if voter_2 == voter_3 in voter_names:
    print(f"{voter_2} is trying to register twice and it is not allowed")
    
voter_4 = input("Kindly enter your name: ")
voter_names.add(voter_4)
if voter_1 == voter_4 in voter_names:
    print(f"{voter_1} is trying to register twice and it is not allowed")
if voter_2 == voter_4 in voter_names:
    print(f"{voter_2} is trying to register twice and it is not allowed")
if voter_3 == voter_4 in voter_names:
    print(f"{voter_3} is trying to register twice and it is not allowed")
    

print(f"The total number of unique voters that registered is {len(voter_names)}")
