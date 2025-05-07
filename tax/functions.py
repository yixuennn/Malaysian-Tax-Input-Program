import pandas as pd
import os

#Save a new registered user to users.csv
def save_user(user_id, ic_number, filename="users.csv"):
    columns = ['User ID', 'IC Number']
    df = pd.DataFrame([[user_id, ic_number]], columns=columns)

    if os.path.exists(filename):
        df.to_csv(filename, mode='a', index=False, header=False)
    else:
        df.to_csv(filename, mode='w', index=False, header=True)

#Load registered users from users.csv and return as a dictionary.
def load_users(filename="users.csv"):
    if os.path.exists(filename):
        df = pd.read_csv(filename,dtype={'IC Number':str})
        return dict(zip(df['User ID'], df['IC Number']))
    else:
        return {}

#Verify the user's credentials
def verify_user(ic_number, password):
    return len(ic_number) == 12 and password == ic_number[-4:]

#Input annual income and tax relief
def get_user_input():
    while True:
        try:
            income = float(input("Please enter your annual income (RM): "))
            relief = float(input("Please enter your total tax relief (RM): "))
            if income < 0 or relief < 0:
                print("Income and relief must be positive. Please Re-enter.\n")
                continue
            return income, relief
        except ValueError:
            print("Invalid input. Please enter NUMERIC values only.\n")

#Calculate tax payable
def calculate_tax(income, tax_relief):
    chargeable_income = max(0, income - tax_relief)
    
    if chargeable_income <= 5000:
        tax = 0
    elif chargeable_income <= 20000:
        tax = (chargeable_income - 5000) * 0.01
    elif chargeable_income <= 35000:
        tax = 150 + (chargeable_income - 20000) * 0.03
    elif chargeable_income <= 50000:
        tax = 600 + (chargeable_income - 35000) * 0.08
    elif chargeable_income <= 70000:
        tax = 1800 + (chargeable_income - 50000) * 0.14
    elif chargeable_income <= 100000:
        tax = 4600 + (chargeable_income - 70000) * 0.21
    else:
        tax = 10900 + (chargeable_income - 100000) * 0.24

    return round(tax, 2)

#Save user's data to CSV file
def save_to_csv(data, filename):
    columns = ['IC Number', 'Income', 'Tax Relief', 'Tax Payable']
    df = pd.DataFrame([data], columns=columns)
    df['IC Number'] = df['IC Number'].astype(str)

    if os.path.exists(filename):
        df.to_csv(filename, mode='a', index=False, header=False)
    else:
        df.to_csv(filename, mode='w', index=False, header=True)

#Read data from a CSV file
def read_from_csv(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename,dtype={'IC Number':str})
    else:
        return None
