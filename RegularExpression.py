# ==========================================
#          DAY 32 REGULAR EXPRESSION
# ==========================================
# to kya haal chal bhi log kaise ho 
# welcome back to day 32 of regular expression 
# to aaj ka topic bohat important hain aur eassy bhi hai 
# to shuru karte hai bina ksisi time pass kiye 
# regular expression ko ham shortcut main regex bhi bolte hai.


# ==========================================
# REGULAR EXPRESSION KYA HOTA HAI ??
# ==========================================
# --> ye pattern text ke andar kuch search karne ke liye use hota hai.
# simple yaad rakho 
# --> Pattern jo text ko search , match ya validate karta hai.

# real life example
# socho tere pass ek notebook hai.
# usme 1000 student ke naam hai.
# aur tuze tera naam dhund na hai
# tu kya karega??
# har line padhega.
# regex bhi ecaxtly yehi karta hai.
# Wo text ke andar pattern search karta hai.

# jaise ke samj lo 
# phone number 
# email valid hai ya nahi
# password main kitne digits , alphabates , numbers & symbol 
# ye sab validate karne ke liye regex ka use karte hai ham log.


# ==========================================
# PYTHON MAIN REGEX KA MODULE
# ==========================================
# use karne ke liye --> import re
# likhne padta hai.
# example.
import re # re(regular expression)


# ==========================================
# SEARCH
# ==========================================
# sabse pehla function.
# code --> re.search()
# ye text ke andar pattern search karta hai.
# example.
import re
text = "I Love Python"
result = re.search("Python",text)
print(result)
# // Output ??? --> <re.Match object ...>

# <re.Match object ...> ??
# matlab python word match ho gaya
# agar nahi milta to 
# // Output ??? --> None
# example.
import re
text = "I Love Python"
result = re.search("Java",text)
print(result)
# // Output ???


# ==========================================
# GROUP()
# ==========================================
# Agar actual matching word chahiye
# example.
import re
text = "Hii My Name Is Sumit"
result = re.search("Sumit",text)
print(result.group())
# // Output ???


# ==========================================
# MATCH()
# ==========================================
# --> match()
# sirf string ke beginning ko check karta hai.
# example.
import re
text = "Python is Easy"
result = re.match("Python", text)
print(result.group())
# // Output ???


# ==========================================
# FINDALL()
# ==========================================
# ye sab matching words return karta hai.
# example.
import re
text = "python java python c++ python"
result = re.findall("python",text)
print(result)
# // Output ???


# ==========================================
# SPLIT()
# ==========================================
# text ko split karta hai.
# example.
import re
text = "apple,mango,banana"
result = re.split(",",text)
print(result)
# // Output ???


# ==========================================
# SUB()
# ==========================================
# Replace karta hai.
# example.
import re
text = "I Love Java"
result = re.sub("Java","Python",text)
print(result)
# // Output ???


# ==========================================
# REGEX SYMBOLS
# ==========================================
# ab aate hai asli magic par.
# Dot ( . )
# matlab : Any one character
# example.
import re
text = "Cat"
print(re.findall("C.t",text))
# // Output ???

# Beginning ( ^ )
# example.
result = re.findall("^Python","Python is easy")
print(result)
# // Output ???


# Ending ( $ )
# example.
result = re.findall("Easy$","Python is Easy")
print(result)
# // Output ???


# Zero ya more times ( * )
# example.
result = re.findall("ab*","ab abb abbb a")
print(result)
# // Output ???


# One more times ( + )
# example.
result = re.findall("ab+","ab abb abbb a")
print(result)
# // Output ???
# notice kiya kya aapne sab match ho gaya pr last vaala
# single a match nahi hua


# Zero ya one time ( ? )
# example.
result = re.findall("colou?r","colour colour")
print(result)
# // Output ???


# ==========================================
# CHARACTER CLASSES
# ==========================================
# [abc]
# matlab: a ya b ya c
# example.
result = re.findall("[abc]","apple ball cat")
print(result)
# // Output ???


# Digits [0-9]
# example.
result = re.findall("[0-9]", "Psumit25")
print(result)
# // Output ???


# Capital letters [A-Z]
# example.
result = re.findall("[A-Z]", "Sumit Is Good In Python")
print(result)
# // Output ???


# Small letters
# example.
result = re.findall("[a-z]","Psumit25")
print(result)
# // Output ???



# ==========================================
# REAL LIFE USE CASE 
# ==========================================
# - Email validation
# - Phone number
# - Password validation 
# - Log file analysis
# - Web scraping
# - Cybersecurity
# - Data cleaning


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1) 
import re
text = "I Love Python"
print(re.search("Python", text).group())
# // Output ???

# 2) 
import re
text = "Python Java Python"
print(re.findall("Python", text))
# // Output ???

# 3)
import re
text = "Apple,Mango"
print(re.split(",", text))
# // Output ???

# 4)
import re
text = "I Love Java"
print(re.sub("Java","Python", text))
# // Output ???

# 5) Regex use karne ke liye konsa module import karte hain ??
# --> inport re 


# ==========================================
# MINI PROJECT
# ==========================================
# email validator 
import re 
email = input("Enter Email : ")
pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
if re.match(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")
# // Output ???

 
# Regex = Pattern jo text ko search, match aur validate karta hai.
# import re

# To finally aaj ka hamar day 32 khatam ,
# aaj ka topic bhi easy tha aur imporatant bhi tha bohat jayad
# to isko 2,3,4 barr revise karle taaki tera aaj ka lecture he complete ho jaye 
# to milte hai kal day 33 main kisi new topic ke saath 
# tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳
