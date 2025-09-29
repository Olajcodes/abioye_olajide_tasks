# #   TASK 2

# 6. Check if a given string contains the substring "python" (case-insensitive)
given_string = input("Enter a word: ")
print("python" in given_string.lower())

# 7. Write a program to reverse a string without using slicing ([::-1])
given_string = "Python"
print(given_string[5], given_string[4], given_string[3], given_string[2], given_string[1], given_string[0])

# 8. Given a string with extra spaces, remove the leading and trailing spaces.
string_with_spaces = "     A String of words to test  "
print(string_with_spaces.strip())

# 9. Ask the user to enter a sentence and print the number of vowels in it
user_input_vowel = input("Kindly provide a sentence: ")
user_input = user_input_vowel.lower() 
print(user_input.count("i") + user_input.count("e") + user_input.count("a") + user_input.count("o") + user_input.count("u"))


# # 10. Convert a string "1234" to an integer and multiply it by 2
string = "1234"