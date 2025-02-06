class ATM:
    def __init_(self):
        self.pin =''
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input("""How can i help you?
              1. create pin
              2. change pin
              3. check balance
              4. withdraw 
              5. Anything else to exit
              """)
        if user_input =='1':
            # create pin
            self.createPin()
        elif user_input =='2':
            #change pin
            self.changePin()
        elif user_input =='3':
            #check balance
            self.checkBalance()
        elif user_input =='4':
            #withdraw
            self.withdraw()
        else:
            self.exit()
    def createPin(self): 
        userPin = int(input("Enter the pin "))
        self.pin = userPin 
        user_balance = int(input("Enter the balance: "))
        self.balance = user_balance
        print("Pin created succesfully") 
    def changePin(self):
        if(int(input("Enter the pin: "))==self.pin):
            changedPin = int(input("Enter the  updated pin : "))
            self.pin = changedPin
            print("Update successfull")
        print("Invalid entry!!")
    def checkBalance(self):
        if(int(input("Enter the pin : "))==self.pin):
            print("The balance is : ",self.balance)
        print("Incorrect pin")
    def withdraw(self):
        if(int(input("Enter the pin: "))==self.pin):
            wd = int(input("Enter the money amount to be withdrawn: "))
            print('Withdraw succes!!\n Updated balance is : ',self.balance-wd)
        print('Bad error!!')
    def exit(self):
        print("Exit succesfull!!")
        return self.menu()

Atm_01 = ATM()
Atm_01.menu()
