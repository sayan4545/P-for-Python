class ATM:
    def __init__(self):
        print(id(self))
        self.pin = ''
        self.balance = 0
        # self.menu()

    def menu(self):
        while True:
            user_input = input("""How can I help you?
                  1. create pin
                  2. change pin
                  3. check balance
                  4. withdraw 
                  5. Anything else to exit
                  """)
            if user_input == '1':
                # create pin
                self.createPin()
            elif user_input == '2':
                # change pin
                self.changePin()
            elif user_input == '3':
                # check balance
                self.checkBalance()
            elif user_input == '4':
                # withdraw
                self.withdraw()
            else:
                print("Exit successful!!")
                break

    def createPin(self):
        userPin = int(input("Enter the pin: "))
        self.pin = userPin
        user_balance = int(input("Enter the balance: "))
        self.balance = user_balance
        print("Pin created successfully")

    def changePin(self):
        if int(input("Enter the current pin: ")) == self.pin:
            changedPin = int(input("Enter the new pin: "))
            self.pin = changedPin
            print("Pin updated successfully")
        else:
            print("Invalid entry!!")

    def checkBalance(self):
        if int(input("Enter the pin: ")) == self.pin:
            print("The balance is: ", self.balance)
        else:
            print("Incorrect pin")

    def withdraw(self):
        if int(input("Enter the pin: ")) == self.pin:
            wd = int(input("Enter the amount to withdraw: "))
            if wd <= self.balance:
                self.balance -= wd
                print('Withdrawal successful! Updated balance is: ', self.balance)
            else:
                print('Insufficient balance!')
        else:
            print('Incorrect pin!!')

Atm_01 = ATM()
print(id(Atm_01))

