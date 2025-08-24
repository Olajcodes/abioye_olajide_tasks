#  Task 1
# For code 1 snippet: It is collecting input (numbers) from users and it is an integer type, asking for the first and second numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# The print functions below is trying to check if num1 is equal to num2 or not and if it's greater than or less than and printing out the boolean answer.
print(f"{num1} == {num2} : {num1 == num2}")

print(f"{num1} != {num2} : {num1 != num2}")

print(f"{num1} > {num2} : {num1 > num2}")

print(f"{num1} < {num2} : {num1 < num2}")

# The 3 usecases one can apply the above program are:
'''
- Pin verification
- Exam pass validation
- Scholarship eligibility
'''

#  A program to change pin
old_pin = int(input("Kindly enter your old pin: "))
new_pin = int(input("Kindly enter your new pin: "))
confirm_new_pin = int(input("Kindly confirm your new pin: "))

confirmation = new_pin == confirm_new_pin
print(f"The pin changed status is {confirmation}")