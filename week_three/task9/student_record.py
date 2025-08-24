# TASK SIX: Word Analyzer
user_input = input("Kindly enter a word: ")

if user_input.isupper() == True:
    print(f"{user_input} is all in uppercase")
else:
    print(f"{user_input} is not in uppercase")
    
if user_input.islower() == True:
    print(f"{user_input} is all in lowercase")
else:
    print(f"{user_input} is not in lowercase")
    
if user_input.istitle() == True:
    print(f"{user_input} is in title case")
else:
    print(f"{user_input} is not in title case")
    

print(f"{user_input} is of length {len(user_input)}.")
