# ==========================================
#         DAY 27 ENCAPSULATION
# ==========================================
# To kya haal chaal bahi log kaise ho aap sab 
# welcome back to our new lecture 
# to aaj ka hamar topic hai Encapsulation bohat aasan hai , aurrr IMP bhi 
# aage jake use main aayega 100% 
# to shuru karte hai bina kisis time pass kiya 


# ==========================================
# ENCAPSULATION
# ==========================================
# --> Data aur method ko ek class ke andar bandh(close) karna aur unnecessary direct access ko rokna.

# samj main nahi aaya hoga , aage pura lectur kr
# Aurr baad main aake defination ko padhn , samj main aayega 

# example:
# soch tere accoun main 50,000 hai aur 
# koi bhi usse use ya access kar sakta hai 
# tera to bank balance main addition ka to pata nahi pr subtraction jarur hoga 
# isliye bank data ko protect karta hai.
# isliye ham encapsulation ka use karte hai
# aur padhna bhi jaruri hai.

# PROBLEM WITHOUT ENCAPSULATION
class bank:
    def __init__(self):
        self.balance = 50,000
account = bank()
account.balance = 3000
print(account.balance)

# Ab dekh.
# original balance = 50,000 tha.
# par bahar se kisi ne direct change kar diya .
# 50,000 ko direct 3000 pe laake rakh diya .
# ye dengerous hota hai.


# ==========================================
# PYTHON PRIVATE VARIBLE 
# ==========================================
# python main private varible banane ke liya :
# --> [ __varible ] Double underscore
# ka use karte hai , kaise wo mai samjaunga
# example.
class bank:
    def __init__(self):
        self.__balance = 50,000
account = bank()
print(account.__balance)
# // Output ???
# Error aayega 

# kyu ki acces nahi milega.
# kyuki varible private(__varible) main store hai.
# to ham isko access karne ke liye method ka use karna padta hai.


# ==========================================
# VALUE ACCESS KARNA
# ==========================================
class bank:
    def __init__(self):
        self.__balance = 60000
    def show_balance(self):
        print(self.__balance)
account = bank()
account.show_balance()
# // Output ???

# hamne yaha pr method ka use kiya hai .
# jab tak ham method ka use nahi karte tab tak access nahi kar sakte.
# ab tumara balance secure hai.


# ==========================================
#  CHANGING VALUE 
# ==========================================
# example.
class bank:
    def __init__(self):
        self.__balance = 20000
    def deposite(self,amount):
        self.__deposite += amount
    def show_balance(self):
        print(self.__balance)
account = bank()
account.deposite(200)
account.show_balance()
# // Output ???

# Step by Step
# account = bank() --> object bana

# balance = 20000 --> store hua.

# deposite:
# account.deposite(200)

# python ne:
# 20000 + 200 kiya.

# new balance:
# 20200 --> ho gaya

# yaha pe tu withdrawal bhi kar sakta hai.
# condition change karne padegi bass.


# ==========================================
# DIRECT ACCESS ABHI BHI NAHI HOGA
# ==========================================
# account.__balance
# output error aayega
# kyuki encapsulation data ko protect kar raha hai.


# ==========================================
# GETTER METHOD
# ==========================================
# getter ka kaam:
# --> value ko read karna
# example.
class student:
    def __init__(self):
        self.__marks = 95
    def get_marks(self):
        return self.__marks
s1 = student()
print(s1.get_marks())
# // Output ???


# ==========================================
# SETTER METHOD
# ==========================================
# --> value update karna.
# example.
class student:
    def __init__(self):
        self.__marks = 95
    def set_marks(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
s1 = student()
s1.set_marks(99)
print(s1.get_marks())
# // Output ???


# ==========================================
# ENCAPSULATION KO TOD KAR SAMAJHO
# ==========================================
# without encapsulation:
# balance = 500
# koi bhi change kar sakta hai.

# with encapsulation:
# __balance
# private ho gaya.

# Access karne ke liye
# get_balance()

# change karne ke liye :
# set_balance()

# Real life Use = 1) banking apps ,2) Instagram ,3) Whatsapp ,4) payment apps ,5) E-Commerce apps
# bhai bohat apps iska use karte hai.


# ==========================================
# PRACTICE TIME 
# ==========================================
# 1)
class Student:

    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks

s1 = Student()

print(s1.get_marks())

# 2)
class Bank:

    def __init__(self):
        self.__balance = 1000

    def show(self):
        print(self.__balance)

b1 = Bank()

b1.show()

# 3)
class User:

    def __init__(self):
        self.__password = "123"

    def get_password(self):
        return self.__password

u1 = User()

print(u1.get_password())

# 4)
class Student:

    def __init__(self):
        self.__marks = 50

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s1 = Student()

s1.set_marks(80)

print(s1.get_marks())

# 5)
class Bank:

    def __init__(self):
        self.__balance = 500

b1 = Bank()

print(b1.__balance)


# ==========================================
# MINI PROJECT
# ==========================================
class bank:
    def __init__(self):
        self.__balance = 0
    def deposite(self,amount):
        self.__balance += amount
    def show_balance(self):
        print("Balance = " , self.__balance)
account = bank()
money = int(input("Enter Amount : "))
account.deposite(money)
account.show_balance()


# Encapsulation = Data ko protect karna aur controlled access dena

# To finally aaj ka hamar day 27 khatam to aaj hamne padha encapsulation
# to bhai bohat assan topic hai aaj ka hamne is lecture main pura samja
# to kuch nahi bass practice kar taaki aur acche se samj sake tu okay,
# to milte hai day 28 main new topic ke saath tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳
 


