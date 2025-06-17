import json
import random
import string
from pathlib import Path

class Bank:
    database = str(Path(__file__).parent / "data.json")
    data = []  # Will be loaded from the file if it exists    @classmethod
    def load_data(cls):
        try:
            if Path(cls.database).exists():
                with open(cls.database) as fs:
                    cls.data = json.load(fs)
                    if not isinstance(cls.data, list):
                        cls.data = []  # Initialize as empty list if not already a list
            else:
                cls.data = []  # Initialize as empty list for new file
                print("No existing data file found. Creating new one.")
        except Exception as err:
            cls.data = []  # Initialize as empty list in case of error
            print(f"An error occurred: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __generateAccNum(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices('!@#$%^&*', k=1)
        acc_id = alpha + num + spchar
        random.shuffle(acc_id)
        return ''.join(acc_id)

    def createAccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "account_number": self.__generateAccNum(),
            "pin": input("Enter your 4 digit pin: "),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("You are not eligible for this bank account")
        else:
            print("Your account has been created successfully")
            for key in info:
                print(f"{key} : {info[key]}")
            print("Please note down your account number and pin for future use")
            Bank.data.append(info)
            self.__class__.__update()

# 👉 Load data before using the class
Bank.load_data()
user = Bank()

print('press 1 for creating the account.')
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money from the bank")
print("press 4 for details")
print("press 5 for updating account details")
print("press 6 for deleting your account")

check = int(input("Please enter your input: "))

if check == 1:
    user.createAccount()
