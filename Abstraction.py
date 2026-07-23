# ==========================================
#           DAY 28 ABSTRACTION
# ==========================================
# to kya haal chal bahi log , welcome backt to day 28
# to aaj ka hamar topic hai abstraction , bhaiii assan topic hai 
# to shuru karte hain bina kisi time pass kiye


# ==========================================
# ABSTRACTION
# ==========================================
# --> User ko sirf important cheeze dikhana 
#     aur andar ka complex logic hide karna.
# bass simple hai 

# real life exmaple.
# soch tu bike chala raha hai.
# bike start karne ke liye = 1) Key lagao, 2) Start button dabao, 3) Bike start
# bas itna hi karta hai.
# # par bike ke andar ka : 1) engine working 2) Fule system 3) battery 4) Wiring
# kaise kaam karte hain?
# ye sab tujhe nahi pata .
# aur pata hona bhi zaroori nahi.
# tu sirf bike use kar raha hai.

# yehi Abstraction hai mere dost 

# ek aur example dekh :
# soch tune ek website banayi hai 
# deploy karne ke baad jo user jo hota hai
# use bass hamar front end dikhta hai 
# to backend to nahi dekhega aur user ko isee kuch jarurat bhi nahi.
# use bass use karna hota hai 


# ==========================================
# ABSTRACTION KI ZARURAT KYU HAI ?
# ==========================================
# Soch agar har user ko software ka poora internal code dekhna pade.
# to software use karna impossible ho jayega.
# isliye:
# Imoportant things -> Show
# Complex logic -> Hide
# isi ko abstraction bolte hain.


# ==========================================
# PYTHON ME ABSTRACTION
# ==========================================
# python mein abstraction ke liye use hota hai:
# PYTHON = ABC aur @abstractmethod
# ye abc module se aata hai.

# example.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# yaha:
# Animal --> ek abstracted class hai.
# Aur:
# Sound()
# ek abstract method hai 


# ==========================================
# ABSTRACTED METHOD KAY HOTA HAI ?
# ==========================================
# abstracted method main mein sirf method ka naam hota hai.
# uska code nahi hota mere dost 
@abstractmethod
def sound(self):
    pass
# yaha sirf batay gaya:
# har animal ko sound() method hona chahiye
# lekin sound kya hoga?
# ye child class decide karegi.


# ==========================================
# CHILD CLASS
# ==========================================
# example.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
d1 = Dog()
d1.sound()
# // Output ???

# parent class ne sirf rule banaya:
# --> sound() hona chahiye 
# dog ne us rule ko implement kiya:
# --> def sound(self):
#         print("Bark")

# agar implement nahi kiya to ?
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    pass
d1 = Dog()
# // Output ???

# kyuki parent ne bola tha:
# --> sound() banana compulsory hai
# Dog ne nahi banaya.
# isliye error aaya.


# ==========================================
# ABSTRACTION KO TOD KAR SAMAJHO
# ==========================================
# parent class:
# --> class Animal(ABC):
# rule banati hai.

# Bastract Method:
# --> @abstractmethod
#     def sound(self):
#         pass
# bolta hai: ye method sab child classes mein hona chahiye.

# Child class:
# --> class Dog(Animal):
#rule follow karti hai.


# ==========================================
# REAL LIFE EXAMPLE
# ==========================================
from abc import ABC, abstractmethod
class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass
# car:
class Car(Vehical):
    def start(self):
        print("Car started")
# bike:
class Bike(Vehical):
    def start(self):
        print("Bike Started")
# object:
c1 = Car()
b1 = Bike()
c1.start()
b1.start()
# // Output ???


# ==========================================
# ENCAPSULATION VS ABSTRACTION
# ==========================================
# Bohat log confuse hote hain.

# Encapsulation:
# --> Data ko protect karna
# example.
# --> self.__balance

# Abstraction:
# complex logic hide karna
# example.
# --> @abstractmethod

# yaad rakh:
# Encapsulation -> protection
# Abstraction -> Hiding Complexity


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1)
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d1 = Dog()

d1.sound()
# // Output ???

# 2)
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Started")

c1 = Car()

c1.start()
# // Output ???

# 3) Shape kis type ki class hai ???
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


# 4) Ye kis type ki method hai ???
@abstractmethod
def show(self):
    pass

# 5) Abstraction ka main purpose kya hai ???


# ==========================================
# MINI PROJECT
# ==========================================
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("Writing Code")
class Tester(Employee):
    def work(self):
        print("Testing Software")
d1 = Developer()
t1 = Tester()
d1.work()
t1.work()
# // Output ???


# Abstraction = User ko sirf important cheeze dikhana aur complex logic hide karna
# --> from abc import ABC, abstractmethod


# to finally aaj hamar day 28 Abstraction khatam ,
# aaj hamne jayad coding nahi sekhe 
# to aaj hamre OOP ke saare major pillars complete ho gaye hai bhai log 
# day 23 se revise kar pure OOP ke lecture ko 
# to kuch nahi thod bohat practice kr aur pichle vaale lecture day 1 se
# revise kar taaki aur acche se samaj mai aaye 
# to chalo milte day 29 main kisi new topic ke saath tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳
 
