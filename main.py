import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An exception occurred: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        return ''.join(random.sample(string.ascii_letters + string.digits + "!@#$%^&*", 7))

    def find_user(self, accnumber, pin):
        return next((i for i in Bank.data if i['accountNo.'] == accnumber and str(i['pin']) == str(pin)), None)

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "You must be 18+ and use a 4-digit PIN."
        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": self.__accountgenerate(),
            "balance": 0
        }
        Bank.data.append(info)
        self.__update()
        return True, info

    def deposit_money(self, accnumber, pin, amount):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "User not found."
        if amount <= 0 or amount > 10000:
            return False, "Amount must be between 1 and 10,000."
        user['balance'] += amount
        self.__update()
        return True, user['balance']

    def withdraw_money(self, accnumber, pin, amount):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "User not found."
        if amount > user['balance']:
            return False, "Insufficient balance."
        user['balance'] -= amount
        self.__update()
        return True, user['balance']

    def view_details(self, accnumber, pin):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "User not found."
        return True, user

    def update_details(self, accnumber, pin, name=None, email=None, new_pin=None):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "User not found."
        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin:
            user['pin'] = int(new_pin)
        self.__update()
        return True, user

    def delete_account(self, accnumber, pin):
        user = self.find_user(accnumber, pin)
        if not user:
            return False, "User not found."
        Bank.data.remove(user)
        self.__update()
        return True, "Account deleted successfully."
