
# from file_ops import save_participant
# from file_ops import load_participants

# from participant_pkg import file_ops

import csv
from pathlib import Path

workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"

participant_dict = {}

# def main():
    # load_participants()     
    # file_ops.load_participants      # Load participants if any any when app starts
    
# while True:
name = input("Kindly enter your name: ")
if name == "":
    print("Name can't be empty! You must provide your name.")
    try:
        age = int(input("Kindly enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
    except ValueError as e:
        print("Oops! That's not a valid age.", e)
        
    except TypeError:
        print("Sorry! We only accept numbers.")
else:
    print("Field must not be empty")
try:
            
    phone_no = int(input("Kindly input your phone number: "))
    if len(phone_no) == 11:
        track = input("Kindly enter your track: ")
    else:
        print("Your phone number must be up to 11 digits.")
except ValueError:
    print("You can only input numbers.")
                
        # return main
            
            
            
            
            
            