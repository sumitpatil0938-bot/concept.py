# ==========================================
#               DAY 19 MODULE
# ==========================================

# To kya haal chal bhai log kaise ho , welcome back to day 19,
# to aaj ham day 19 main padne ja rahe hai module ke baare mai detail main,
# aaj jayda coding nahi hai bass thodi hain aur practicle karke dekhenge matlab 
# jaise jaise mai bolta hu bass waise waise he karte jana 

# To shuru karte hain bina kisi times pass kiye , okay

# ==========================================
# MODULE
# ==========================================
# --> module matlab python ke filr creat karna .
# haa bass wahi meaning hai [ python file(.py) = Module ]
# python ke file kaise banate hain 
# file ka naam daalo aur uske aage .py laga do 
# example.
# 1) Recursion.py. 2) Modules.py. 3) Tuple.py and ect....
# file ko ham module bolte hain , bass khatam

# aise ham file creat kar sakte hai
# sooch sooch, ek company ka project 60,000 lines ka hai,
# kya sab code ek hi file mein likhenge ? nahi na 
# isliye python mein code ko alag alag files mein divide karte hain 
# aur un files ko ham (MODULE) bolte hain.


# ==========================================
# MODULE KE NEED ??
# ==========================================
# soch tune calculator banaya
# aur tuze wo code firse dusre project main use karna ho ,
# to tu use code ko doobara to nahi likhega na 
# iske liye ham iska use karte hain , kaise wo aage mai bataunga 

# START 

# Ham pehla modulue banate hain

# File 1 --> maths.py 
# uske andar code likh 

# --> def add(a,b):
#        return(a+b)


# File 2 --> main.py
# uske andar code likh

# --> import maths
#     print(maths.add(10,20))

# // Output ??? check kar leoo

# kais kiya ?? explain karta hu 
# Step by step

# python ne dekha 
# import maths 

# matlab --> jao maths.py file lekar aao.
# fir
# maths.add(10,20)

# matlab --> maths.py ke andar jo add() function hai use run karo.
# // Output ???


# ==========================================
# IMPORT
# ==========================================
# import ka use ham module ko use karne ke liye use karte hain .
# (import)
# example.
# import maths
# matlab --> math module ko current file mein le aao .


# ==========================================
# BUILT IN MODULE 
# ==========================================
# python kuch module pehle se he deta hai 
# use ham BUILT-IN MODULE bolte hain.
# example.
# 1) math
# 2) random
# 3) os
# 4) datetime


# MATH MODULE 
# ye math related kaam karte hai.
# example.
# 1) 
import math
print(math.sqrt(25))   # sqrt(square root)    
#    // Output ???

# 2) 
import math
print(math.factorial(5))
#    // Output ???

# 3) 
import math
print(math.pi)
#    // Output ???


# RANDOM MODULE 
# random values generate karta hain.
# example.
# 1) 
import random
print(random.randint(1, 10))
#    // Output ??? kuch bhi aa sakta hain 1-20 ke bich main ke .

# RANDIANT()
# syntax: random.randiant(start, end)
# example.
# same example from random module


# ==========================================
# RANDOM CHOICE
# ==========================================
# kuch alag nahi ahi isme bass randiant ko choice ke saath replace kar do
# example.
import random
fruits = ["apple","mangos","banana"]
print(random.choice(fruits)) # // Output ???

# matlab alag alag baar alag alag output milenga 


# ==========================================
# SPECIFIC FUNCTION IMPORT KARNA 
# ==========================================
# normal 
import math
print(math.sqrt(64))

# shortcut.
from math import sqrt
print(sqrt(81)) # // Output ???

# ab baar baar (math.) jo ham print karte waqt likthe the wo likhne ki zarurat nahi hai.


# ==========================================
# MULTIPLE FUNCTION IMPORT
# ==========================================
# example se samj ja 
# example.
from math import sqrt,factorial
print(sqrt(81)) # // Output ???
print(factorial(10)) # // Output ???



# ==========================================
# ALIAS KYA HOTA HAI ???
# ==========================================
# alias ka matlab nickname hota hai.
# exmple.
# import math as m
# yaha pr math ka naam badal ke m kar diya hai
# ab pura math likhne ke jarurat nahi hai 
# example.
import math as su
print(su.sqrt(25)) # // Output ???


# ==========================================
# USER DEFINED MODULE
# ==========================================
# ham khud bhi module bana sakte hain.
# example.
# make module --> sumit.py --> code likho
# def hello():
#    print("i love you sumit")

# in another module --> code likho
# impor sumit
# sumit.hello() # // Output ???


# ==========================================
# FLOW OF MODULE
# ==========================================
# Step 1
# module banao --> maths.py

# Step 2
# import karo --> import math

# Step 3
# use karo --> maths.add()

# bas...khatam


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1)
import math
print(math.sqrt(49)) # // Output ???

# 2)
import math
print(math.factorial(4)) # // Output ???

# 3)
from math import sqrt
print(sqrt(100)) # // Output ???

# 4)
import random
print(random.randint(1, 5)) # // Output ???

# 5)
import math as m
print(m.pi) # // Output ???


# ==========================================
# MINI PROJECT 
# ==========================================
# Q) luck number vaala project generate karo , user se input lekar ??

# code 
import random
name = input("Enter Your Name : ")
number = random.randint(1, 100)
print("Hello", name)
print("Your Lucky Number Is :", number)


# to finally aaj ka hamar day 19 khatam to aaj hamne jayda code nahi kiya balki samja code ko kaise reuse kare ,
# taaki hamar time bach sake , to milte hain hamare agle lecture main tab tak ke liya ,

# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳






