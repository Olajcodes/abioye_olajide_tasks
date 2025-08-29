
# from file_ops import save_participant
# from file_ops import load_participants

# from participant_pkg import file_ops

# import csv
# from pathlib import Path

# workspace = Path("workspace")
# workspace.mkdir(exist_ok= True)
# csv_file = workspace / "contacts.csv"

# participant_dict = {}

def main():
    # load_participants()     
    # file_ops.load_participants      # Load participants if any any when app starts
        
    while True:
        # Collecting and Validating name input.
        while True:
            try:
                name = input("Kindly enter your name: ")
                if name == "" :
                    print("Name can't be empty! You must provide your name.")
                elif name.isalpha() == False:
                    raise ValueError("Only Alphabets required.")
                else:
                    break
            except ValueError as e:
                print("Oops!", e)

        #  Collecting and Validating Age
        while True:
            try:
                age = int(input("Kindly enter your age: "))
                if age <= 13:
                    print("Sory! You're too young to participate.")
                    if age < 0:
                        
                elif age >= 
                else:
                    break
            except ValueError:
                print("Oops! That's not a valid age.\nYou can only provide positive numbers.")

        # Collecting and Validating Phone number
        while True:
            try:
                phone_no = input("Kindly input your phone number (Country code not accepted): ")
                if len(phone_no) != 11:
                    print("Your phone number must be exactly 11 digits. Try again.")
                elif phone_no.isnumeric() == False:
                    print("Invalid entry. No country code please.")
                else:
                    break
            except ValueError:
                print("You can only input numbers")
            except TypeError:
                print("It can only check for length of strings and not integers")

        #  Collecting and Validating Track input
        while True:
            try:
                track = input("Kindly enter your track: ")
                if track.isalpha() == False:
                    raise ValueError("Must only be Alphabets")
                else:
                    break
            except ValueError as e:
                print("Oops!", e)
                        
main()
            
            
            
            
            
            