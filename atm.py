class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("₹ 10000")

    def withdrawl(self,money):
        new_amount = 10000 - money
        print("You have withdrawn amount "+str(money) + ". Your remaining balance is "+ str(new_amount))      


def main():
    print("Welcome to Gringotts Bank! The wizards and witchs bank")
    Account = input("Please enter your acount image or number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        money = int(input("enter amount you want to enter"))
        new_user.withdrawl(money)

    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()