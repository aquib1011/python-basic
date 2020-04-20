# April 17, 2020

# Priyanshul Govil
# 19070124053
# IT - 3

# PPSL Assignment -
# Write a python program to create a sales system for car dealership using Object-oriented techniques.

class Payment:
    def __payCash(self, amount):
        print("Mode of Payment : CASH")
        print("Amount received = {} INR ".format(amount))
        
    def __payCard(self, amount):
        print("Mode of Payment : CARD")
        _cardNum = input("Enter Card Number : ")
        _otp = input("Enter OTP received : ")
        print("Amount received = {} INR ".format(amount))

    def __payCheque(self, amount):
        print("Mode of Payment : CHEQUE")
        _chequeNum = input("Enter cheque number of received cheque : ")

    def payment_(self, amount):
        print("1. CASH\n2. CARD\n3. CHEQUE")
        paymentMethod = int(input("\nEnter payment method : "))
        print()

        if(paymentMethod == 1):
            self.__payCash(amount)
        elif(paymentMethod == 2):
            self.__payCard(amount)
        elif(paymentMethod == 3):
            self.__payCheque(amount)

        print("\n******** TRANSACTION APPROVED ********\n")


class Car(Payment):
    def __init__(self, carList: dict):
        self.carList = carList

    def __printCarList(self):
        for key in self.carList.keys():
            print(key, ".", end = "  ")
            for detail in self.carList[key]:
                print("\t", detail, end = " ")
            print(" INR")

    def buyChoice(self):
        self.__printCarList()
        choice = int(input("\nEnter S.No. of Car : "))
        print()
        self.car = self.carList[choice][0]
        self.amount = self.carList[choice][1]

    def generateInvoice(self):
        print("\n**************************************************\n")
        print("Car : ", self.car)
        print("Amount : {} INR\n".format(self.amount))
        super().payment_(self.amount)


class Customer:
    def __init__(self):
        self.detailList = {}
    
    def addData(self, name, contactNum, emailID, license, carPurchased):
        self.detailList.update({contactNum : [name, contactNum, emailID, license, carPurchased]})

    def printData(self, contactNum):
        _data = []
        for detail in self.detailList[contactNum]:
            _data.append(detail)

        print("Name : {}".format(_data.pop(0)))
        print("Contact Number : {}".format(_data.pop(0)))
        print("E-Mail ID : {}".format(_data.pop(0)))
        print("License Nubmer : {}".format(_data.pop(0)))
        print("Car Purchased : {}".format(_data.pop(0)))
    
    def printAllData(self):
        for key in self.detailList.keys():
            self.printData(key)
            print()

class CarSales(Customer, Car):
    def __init__(self, data: dict):
        Car.__init__(self, data)
        Customer.__init__(self)

    def __get_userData(self):
        self.name = input("Enter customer' s name : ")
        self.phoneNum = input("Enter customer' s contact no. : ")
        self.mailID = input("Enter customer' s email ID : ")
        self.license = input("Enter customer' s DL no. : ")

        super().addData(self.name, self.phoneNum, self.mailID, self.license, self.car)

    def transaction(self):
        print("*********** BILLING ***********")
        print()
        super().buyChoice()
        self.__get_userData()
        super().generateInvoice()
        super().printData(self.phoneNum)
        print("\nThank You for purchasing!\n")


# driver to test working of program

print("Welcome to THE CAR SELLERS!")
print()

temp_carList = {1: ["Jeep Compass", "20,00,000"],
                2: ["Hyundai Creta", "17,50,000"],
                3: ["Ford Ecosport", "14,00,000"]}

carSales_ = CarSales(temp_carList)

# testing for 2 inputs
for i in range(2):
    carSales_.transaction()

print("**************************************************")
print("\nDetails of all transactions till now are :-\n")

carSales_.printAllData()

print("\n**************************************************")