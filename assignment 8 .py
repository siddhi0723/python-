#ENCAPSULATION AND DATA HIDING
class BankAccount:
    def __init__(self, name, balance):
        self.name = name          
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


# object creation
acc = BankAccount("Vedanti",6789)

# accessing 
print("Account Holder:", acc.name)

# accessing 
print("Balance:", acc.get_balance())

# deposit  amount
acc.deposit(2344)
print("Updated Balance:", acc.get_balance())

#DEVELOPING A LIBRARY CLASS

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


# creating object
my_book = Book("The Midnight Library", "Matt Haig")

# accessing the attributes
print(my_book.name)
print(my_book.author)

#INSTANCE VARIABLES AND METHODS
class Student:
    def __init__(self, name, marks):
        self.name = name        
        self.marks = marks     

    def display(self):          
        print("Name:", self.name)
        print("Marks:", self.marks)


# object 
v1= Student("Vedanti Thorat", 85)

# calling 
v1.display()