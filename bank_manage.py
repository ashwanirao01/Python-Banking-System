import json 
import random 
import string 
from pathlib import Path

class bank :
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs :
                data = json.load(fs)
        else : 
            print("on such file exist ")
    except Exception as err :
        print(f"an Exception occured as {err}")  
        ## save data  in json file 
        
    @staticmethod
    def __update():
        with open(bank.database,'w') as fs:
            fs.write(json.dumps(bank.data))
        
    ## generate account number 
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k= 3)
        num = random.choices(string.digits , k =3)
        spchar = random.choices("!@#$%&*^", k = 1)
        id = alpha + num + spchar 
        random.shuffle(id)
        return "".join(id)
        
    
    def createaccount(self):
        info = {
            "name" : input("Please tell your name : "),
            "age" : int(input("Enter your age : ")),
            "email" : input("Enter your email :- "),
            "pin" : int(input("Enter your 4 number  pin : ")),
            "Account_no" : bank.__accountgenerate(),
            "Balance" : 0
            
        }
        
        if info['age']< 18 or len(str(info['pin'])) != 4 :
            print("sorry you cannot create your account")
        else :
            print("account has been created successfully")
            for i in info : 
                print(f"{i}: {info[i]}")
            print("Please note down your account number ")
            
            bank.data.append(info)
            # call json in file 
            bank.__update()
        
    def depositmoney(self):
        accountno = input("Pleases enter your account number : ")
        pin = int(input("Enter the your pin "))   
    
        userdata = [i for i in bank.data if i['Account_no'] == accountno and i['pin']== pin]
        
        if userdata == False :
            print("Sorry no data found")
            
        else :
            amount = int(input("How much you want to depoit"))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000")
            
            else :
                userdata[0]['Balance'] += amount
                bank.__update()
                print("amount deposit successfully ")  
            
    
    def withdrawmoney(self):
        accountno = input("Pleases enter your account number : ")
        pin = int(input("Enter the your pin "))   
            
        userdata = [i for i in bank.data if i['Account_no'] == accountno and i['pin']== pin]
                
        if userdata == False :
            print("Sorry no data found")
                    
        else :
            amount = int(input("How much you want to withdraw"))
            if userdata[0]['Balance'] < amount:
                print("sorry you don't have that much money ")
                    
            else :
                userdata[0]['Balance'] -= amount
                bank.__update()
                print("amount withdraw successfully ") 

    def showdetails(self):
    
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found ")
        
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name or press enter : "),
                "email":input("please tell your new Email or press enter to skip :"),
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

            bank.__update()
            print("details updated successfully")


    def Delete(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no such data exist ")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = bank.data.index(userdata[0])
                bank.data.pop(index)
                print("account deleted successfully ")
                bank.__update()

user = bank()
print("Press 1 for creating an account")
print("Press 2 for Deposititing the money ")
print("Press 3 for withdrawing the money ")
print("Press 4 for details ")
print("Press 5 for updating the details ")
print("Press 6 for deleting your account ")

check = int(input("Tell your response :-"))

if check == 1:
    user.createaccount()
    
if check == 2:
    user.depositmoney()
    
if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()
