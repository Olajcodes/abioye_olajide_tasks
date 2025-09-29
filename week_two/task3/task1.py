# # TASK 1

# 1. Program to accept a string input from user and display it in uppercase
string_input = input("Kindly provide your first name: ")
print(string_input.upper())

# 2. Given the string "python", print its first and last characters.
given_string = "python"
print(given_string[0], given_string[-1])

# 3. Ask the user for their name and print "Hello, ! the user name."
user_name = input("What\'s your name?: ")
print("Hello,!", user_name)

# 4. Write a program to count the number of characters in a string without using len().
character = input("Enter a word: ")
character_length = character.find(character[-1]) + 1
print(character_length)

# 5. Given "Hello World", replace "World" with "Python"
given_string = "Hello World"
print(given_string.replace("World","Python"))