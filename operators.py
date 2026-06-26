# ==========================================
#           OPERATORS - DAY 5
# ==========================================

# kya haal chal bhai log kaise ho , sab thik
# day 4 ki practice ki ya nahi

# chalo shuru karte hai day 5

# OPERATORS ---> ek types ke symbols hote hai jo values ya variables par operations perform karte hai.
# operators wo cheez hai hai jo python ko batata hai ki numbers ko values ke saath kya kam karna hai.
# ABB SAMJA!!


# ==========================================
# EXAMPLE
# ==========================================

# 10 + 5
# ab yaha pe 10 aur 5 ko "operand" bolte hai
# aur jo '+' hai use operator bolte hai

a = 5
b = 4

print(a + b)  # // output dekhlena


# ==========================================
# TYPES OF OPERATORS
# ==========================================

# Python mein mainly:

# 1). Arithmetic Operators
# 2). Assignment Operators
# 3). Comparison Operators
# 4). Logical Operators
# 5). Identity Operators
# 6). Membership Operators
# 7). Bitwise Operators

# Ab ek-ek karke samajhte hain.


# ==========================================
# 1) ARITHMETIC OPERATORS
# ==========================================

# ye jo operators hai wo sab maths mai use hote hai

# Operators         Meaning
# +                 Addition
# -                 Subtraction
# *                 Multiplication
# /                 Division
# %                 Modulus
# **                Power
# //                Floor Division

# chal ab ek ek krke ise samjte hai

# OYEEE TUUUU HAA TUUU dhyan se sunn
# ab baar barr nahi bolunga
# bohat easy hai bass thoda sa dimak laga le

# aur haa output kya aayega tu khud karke dekh lee
# jab tak practice nahi karega tab tak kuch nahi hoga


# Addition
a = 3
b = 2

print(a + b)  # // Output ???


# Subtraction
a = 3
b = 2

print(a - b)  # // Output ???


# Multiplication
a = 3
b = 2

print(a * b)  # // Output ???


# Division
a = 10
b = 2

print(a / b)  # // Output ???

# ab dekh tu iska output jo hai wo float mai aayega
# tu khud ise convert krle integer main
# agar nahi aata to ek bar day 4 ko revise kr


# Modulus
a = 10
b = 3

print(a % b)  # // Output ???

# Modulus ka output hamesha Remainder aata hai


# Power
a = 3
b = 2

print(a ** b)  # // Output ???


# Floor Division
a = 10
b = 3

print(a // b)  # // Output ???

# ye floor division exact vale deta hai

a = 10
b = 3

print(a / b)  # // Output 3.3333333333333335

# pr agar tu floor division krta hai
# to tuje float mai nahi integer mai aayega output.


# ==========================================
# 2) ASSIGNMENT OPERATORS
# ==========================================

# variable mai values add karne ke liye use hota hai

# "="
x = 10


# "+="
x = 10

x += 5

print(x)  # // Output ???

# as same as "x = x + 5"


# "-="
x = 10

x -= 3

print(x)  # // Output ???

# as same as "x = x - 3"


# ==========================================
# 3) COMPARISON OPERATORS
# ==========================================

# ye jo operator hai 2 values ko compare karta hain
# result hamesha "True" ya "False" he aayega


# Equal to "=="
print(10 == 10)  # // Output ???


# Not equal to "!="
print(10 != 5)  # // iska output kya aayega dekho


# Greater than ">"
print(20 > 10)  # // Output ???


# Less than "<"
print(5 < 10)  # // Output ???


# Greater than equal to ">="
print(10 >= 10)  # // Output ???


# Less than equal to "<="
print(5 <= 10)  # // Output ???


# ==========================================
# 4) LOGICAL OPERATORS
# ==========================================

# condition ko combine karne ke liye use hota hai
# isme 3 conditions hai "AND", "OR" aur "NOT"


# AND
# isme dono condition true hone chahiye
# agar ek bhi condition false aaye
# to output bhi false he aayega

print(True and True)  # // Output ???
print(True and False)  # // Output ???


# OR
# isme ek bhi condition true agar hain
# to output true aayega

print(True or False)  # // Output ???


# NOT
# true ko false aur false ko true bana deta hai

print(not True)  # // Output ???

# isme not true bola hai
# to sedhi baat hai output false he aayega


# Example
age = 20

print(age >= 18 and age <= 60)

# abb tu khud se dekh
# age >= 18  --> True
# age <= 60  --> True
# bich mai konsa operator use hua hai dekh "and" use hua hai 
# // Output ???


# ==========================================
# 5) IDENTITY OPERATORS
# ==========================================

# isme jayda demak mat laga easy hai
# ye bass check karte hain ki dono variables
# same object ko refer kar rahe hain ya nahi

# isme 2 conditions hai 
# "IS" aur "IS NOT"

a = 10
b = 10

print(a is b)  # // Output ???


# IS NOT
a = 10
b = 10

print(a is not b)  # // Output ???


# ==========================================
# 6) MEMBERSHIP OPERATORS
# ==========================================

# ye dekhta hai ke jo values hmne add ki hai
# wo collection ke andar hai ya nahi

# iske bhi 2 conditions hai
# "IN" aur "NOT IN"


# IN
fruits = ["Apple", "Mango", "Banana"]

print("Mango" in fruits)  # // Output ???


# NOT IN
fruits = ["Apple", "Mango", "Banana"]

print("Orange" not in fruits)  # // Output ???


# ==========================================
# 7) BITWISE OPERATORS
# ==========================================

# ye binary numbers pe kaam karta hai
# to ye sach mai beginners ke liya thoda confusing ho sakta hai

# to ham ise baad mai cover karte hai
# kuch lectures ho jane do
# baad mai hmm isee acche se samjte hai okay


# ==========================================
# PRACTICE PROBLEMS
# ==========================================

# 1)
a = 20
b = 10

print(a + b)  # // Output ???


# 2)
a = 10
b = 4

print(a % b)  # // Output ???


# 3)
a = 5
b = 10

print(5 > 10)  # // Output ???


# 4)
print(True and False)  # // Output ???
print(True or False)   # // Output ???


# 5)
fruits = ["Apple", "Mango"]

print("Mango" in fruits)  # // Output ???


# ==========================================
# SUMMARY
# ==========================================

# Operator ek special symbol hota hai
# jo values ya variables par koi operation perform karta hai,
# jaise addition, subtraction, comparison ya logical checking.

# Milte hai day 6 main byeee