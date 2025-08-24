#   Simulated USSD Menu Interaction

print("Welcome to 9JA Parrot Network!")

while True:
    user_dial = input("Kindly dial *200# to proceed: ")
    if user_dial == "*200#":
        print("The available service options are:\n1:  Check Balance\n2:  Buy Airtime\n3:  Buy Data")

        user_choice = input("Choose an option from the above menu: ")

        #  Implementing control flow structure
        available_balance = 10000
        if user_choice == "1":
            print(f"The option selected is to check balance.")
            print(f"The available balance is #{available_balance:,}")
        elif user_choice == "2": 
            print(f"The option selected is to buy airtime.")
            amount = int(input("Kindly enter the amount to buy: "))
            if amount <= available_balance:
                print(f"#{amount:,} airtime has been purchased. The remaining balance is #{available_balance - amount:,}")
            else:
                print("Insufficient balance!")
        elif user_choice == "3":
            print(f"The option selected is to buy data.")
            amount = int(input("Kindly enter the amount to buy: "))
            if amount <= available_balance:
                print(f"#{amount:,} worth of data has been purchased. The remaining balance is #{available_balance - amount:,}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid options! Try again.")
        

        print("After the welcome message screen, the User dialed *200# to display the available options from which the user selected the choice and a confirmation message was displayed.")

        break
    else:
        print("Kindly enter the correct code.")

