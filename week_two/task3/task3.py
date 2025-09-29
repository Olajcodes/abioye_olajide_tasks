 # #  TASK 3

# # 11. Given "apple,banana,orange", split the string into a list of fruits
given_fruits_string = "apple,banana,orange"
print(given_fruits_string.split(","))

# # 12. Ask the user for a sentence and print each word on a new line
user_input = input("Enter a sentence: ")
input_splitted = user_input.split()
print(*input_splitted, sep='\n')

# 13. Replace all spaces in a string with underscores(_)
string_with_spaces = "I love Programming."
print(string_with_spaces.replace(" ", "_"))

# 14. Count how many times the letter "a" appears in "Banana".
string_1 = "Banana"
print(string_1.count("a"))

# 15. Check if a given string starts with "https://"
given_string = input("Enter your word: ")
print(given_string.startswith("https://"))
