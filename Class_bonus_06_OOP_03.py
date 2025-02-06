class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def __str__(self):
        return '{}..{}..{}'.format(self.name,self.gender,self.address)
    def print_address(self):
        print(self.address.city,self.address.getPin(),self.address.state)
    def edit_profile(self,newName,newCity,newPin):
        self.newName = newName
        self.address.edit_address(newCity,newPin)

class Address:
    def __init__(self,city,pin,state):
        self.city = city
        self.__pin = pin
        self.state = state
    def __str__(self):
        return '{}|{}|{}'.format(self.city,self.getPin(),self.state)
    def getPin(self):
        return '{}'.format(self.__pin)
    def setPin(self,pin):
        self.__pin =pin
    def edit_address(self,newCity,newPin):
        self.city = newCity
        self.setPin(newPin)
a1 = Address('Bengaluru',560045,'Karnataka')
p1 = Customer('Chandrika','F',a1)
print(p1)
p1.print_address()
a1.edit_address('Kolkata',989898)
print(a1)
