import functions
from functions import get_user_input
import pandas as pd

FILENAME = 'tax_data.csv'
USERS_FILE = 'users.csv'

def main():
    print("---- Malaysian Tax Input Program ----")

    # Load registered users from file
    registered_users = functions.load_users(USERS_FILE)

    user_id = input("Enter your User ID: ")

    if user_id not in registered_users:
        # Registration
        print("---- New User Registration ----")

        while True:
            ic_number = input("Please enter your 12-digit IC Number (without -): ")
            password = input("Please set your password (last 4 digits of IC): ")

            if functions.verify_user(ic_number, password):
                functions.save_user(user_id, ic_number, USERS_FILE)
                registered_users[user_id] = ic_number
                print("Successfully Registered!")
                break
            else:
                print("Invalid IC format or password. Registration failed!")
                print("----Please Re-enter----")
    else:
        # Existing user login
        ic_number = registered_users[user_id]
        password = input("Please enter your password (last 4 digits of IC): ")

        if not functions.verify_user(ic_number, password):
            print("Login failed! Incorrect password.")
            return

    # Annual Income and Tax Relief
    income, relief = get_user_input()

    # Tax Payable Calculation
    tax = functions.calculate_tax(income, relief)
    print(f"Your tax payable is: RM{tax:.2f}")

    # Save data to CSV
    user_data = [ic_number, income, relief, tax]
    functions.save_to_csv(user_data, FILENAME)
    print("Your data has been saved to the CSV file.")

    # Display all records
    print("\n---- Tax Records ----")
    df = functions.read_from_csv(FILENAME)
    if df is not None:
        print(df.to_string(index=False))
    else:
        print("No records found.")

if __name__ == "__main__":
    main()
