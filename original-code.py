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
                data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"an exception occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age": int(input("tell your age :- ")),
            "email": input("tell your email :- "),
            "pin": int(input("tell your 4 number pin :- ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and int(i['pin']) == pin]

        if not userdata:
            print("sorry no data found")
            return # ❗STOP execution here if no match

        else:
            amount = int(input("how much you want to deposit "))
            if amount > 10000 or amount <= 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0")
                return
            else:
                # print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"Amount deposited successfully and your new balance is {amount}")


    def withdrawmoney(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and int(i['pin']) == pin]

        if not userdata:
            print("sorry no data found")
            return # ❗STOP execution here if no match

        else:
            amount = int(input("how much you want to withdraw "))
            if amount > 10000:
                print("sorry the amount is too much you can withdraw below 10000")
            elif amount >= userdata[0]['balance']:
                print("you dont have enough money in your account")
            else:
                # print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"Amount withdrawn successfully and your new balance is {userdata[0]['balance']}")


    def viewdetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and int(i['pin']) == pin]

        if not userdata:
            print("sorry no data found")
            return

        else:
            print("Your information are \n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found ")

        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name or press enter : "),
                "email": input("please tell your new Email or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")


    def deleteaccount(self):
        accnumber = input("please tell your account number ")
        pin = input("please tell your pin as well ")

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("sorry no data found")

        else:
            choice = str(input("Press 'y' to confirm delete account or press 'n' : "))
            if choice == 'N' or choice == 'n':
                print("Your account delete request has been cancelled. ")
                return
            else:
                indexed = Bank.data.index(userdata[0])
                Bank.data.pop(indexed)
                Bank.__update()
                print("Your account has been deleted successfully. ")






user = Bank()
print("press 1 for creating an account")
print("press 2 for Depositing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.viewdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteaccount()