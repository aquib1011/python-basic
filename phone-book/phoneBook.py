# April 17, 2020

# Priyanshul Govil
# 19070124053
# IT - 3

# PPSL Assignment -
# Python program for a database of phone numbers could be stored 
# using a dictionary and perform Initialize, adding, removing operations.

class PhoneBook(dict):
    def numberAdd(self, name, number):
        if(name in super().keys()):
            print("Sorry, that name already exists in the phone book!")
        else:
            super().update({name: number})

    def numberRemove(self, name):
        keyExist = super().pop(name, False)
        if(not keyExist):
            print("Sorry, that name does not exist in the phone book!")

    def numberSearch(self, name):
        number = super().get(name, -1)
        return number

def programDriver(phone_book: PhoneBook):

    print("1.   Add phone number.")
    print("2.   Remove phone number.")
    print("3.   Search phone number.")
    print("4.   Exit")
    
    choice = int(input("\nPlease press your choice number : "))

    if(choice == 1):
        name = input("Enter name of contact : ")
        number = input("Phone number of contact : ")
        phone_book.numberAdd(name, number)

    elif(choice == 2):
        name = input("Enter name of contact : ")
        phone_book.numberRemove(name)

    elif(choice == 3):
        name = input("Enter name of contact : ")
        number = phone_book.numberSearch(name)
        if(number == -1):
            print("Sorry, that name does not exist in the phone book!")
        else:
            print("Phone number of {} is {}".format(name, number))
    
    elif(choice == 4):
        return False

    else:
        print("Sorry, wrong input!")

    return True

print("Hi! Welcome to the Phone Book.")
phone_book = PhoneBook()

flag = True
while(flag):
    print()
    flag = programDriver(phone_book)