# ==========================================
#               DAY 7 STRING
# ==========================================

# to kya haal chal bhai log aagaye vaapas day 7 maine
# to aaj ka hamara topic hain sring to hmm shurvat se padenge kya hota hai string
# dekhh jo bhi kaam kar raha ho na to usmi jyada time aur dimak mat laga na
# bass daily ke daily consistency se karna


# ==========================================
# STRING
# ==========================================

# STRING --> Abhi tak tune jo bhi padha hai to unta to samaj gaya hoga string kya hota hai ,
# pr agar nahi janta to tension maat le tera bahi abhi bhi hai tere saath
# jise ham single quote ('') ya double quote (" ") maine likhte hai ,
# usee python string maanta hai

# example.

name = "sumit"  # Output ???
name = 'sumit'  # Output ???

# isme jo sumit hai use hm string bolte hain ,
# sumit ke alawa kuch bhi ho sakta haine

# agar hamne kisi bhi number ko quots maine likh diya to python use integer nahi mante
# string maante hai

# example.

age = "22"  # Output ???

# abhi samjha na kuch ,
# to chal ab aage badte hain


# ==========================================
# STRING KO ACCESS KAISE KARTE HAI ??
# ==========================================

# ab ise dhya se dekh

# jab hm kisi text ko ya no. ko string main likhte hain to ,
# python use ek ek karke divide karta hai

# nahi samjha hoga pata hai
# example ke saath samjte hain

# example.

name = "sumit"  # string hai okay

# to ab python ise aise dekhta hain

# S U M I T
# 0 1 2 3 4

# ye jo concept hai use hmm indexing bolte hai

# ab ham indexing ko padte hai


# ==========================================
# INDEXING
# ==========================================

# isme 2 types to nahi bol sakte pr method bol sakte hain

# 1) INDEXING
# 2) NEGATIVE INDEXING


# ==========================================
# 1) INDEXING
# ==========================================

# bass isee tu kuch is taraha se samaj ja

# zero se start hote hai aur jitni badi string hai
# waha tak chalta hain

# example ke saath he samjte hain

name = "sumitpatil"

# S U M I T P A T I L
# 0 1 2 3 4 5 6 7 8 9

name = "mangesh talikote"

# M A N G E S H   T A L I K O T E
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

# jo space hai na use bhi count karta hain

# python ise kuch is taraha se padta hai

# example solve karte hai ise print kaise kara jata hain

name = "sumit"
print(name[3])  # Output ???

name = "mangesh talikote"
print(name[7])  # Output ???

# soch lo tum khud se agar string badi hai aur tumhai last no. print karna hain to kaise kare

# starting se count to nahi karega na

# iske liye hota hai negative indexing


# ==========================================
# 2) NEGATIVE INDEXING
# ==========================================

# negative indexing -1 se shuru hota hai jab tak starting point na aajaye string

# rukk rukk samjata hu

name = "sumit"

# S U M I T
# -5 -4 -3 -2 -1

name = "sahil marne"

# S A H I L  M A R N E
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# ab "sumit" main -1 jo hain wo 'T' ko represent karta hain

# bass etna assan hai

# iske bhi exampke solve karte hain

name = "sumit"
print(name[-1])  # Output ???

name = "sahil marne"
print(name[-6])  # Output ???

# bass etna assan hai bass karle


# ==========================================
# STRING LENGTH
# ==========================================

# kuch nahi string ke size kitne hai ,
# use ham string length bolte hai

# example.

name = "SUMIT"
print(len(name))  # Output ???

# bass kuch nahi karna

# length pata karni ho string ke to
# "len" laga dena print main


# ==========================================
# STRING CONCATENATION
# ==========================================

# ye bhi easy hain bahii

# Do string ko jodne ko bolte hain string concatenation

# example.

name1 = "sumit"
name2 = "patil"

print(name1 + name2)  # Output ???

# agar dono name ke bich main space laga na ho to bass quote add kar do

name1 = "sumit"
name2 = "patil"

print(name1 + " " + name2)  # Output ???


# ==========================================
# STRING REPETITION
# ==========================================

# ek string ko multiple times print karne ko string repetition bolte hain

# example.

nme = "sumit"
print(nme * 5)  # Output ???


# ==========================================
# UPPER CASE
# ==========================================

# string ko capital karta hain

# example.

name = "sumit"
print(name.upper())  # Output ???

# isme kuch nahi karna bass print karte samay "upper" likh dena


# ==========================================
# LOWER CASE
# ==========================================

# string ko samll karne main help karta hain

# example.

name = "SUMIT"
print(name.lower())  # Output ???


# ==========================================
# CAPITALIZATION
# ==========================================

# isme aur upper case main difference hain

# upper case main hmm string ke pure letters ko capital karte hain

# aur capitalization main bass first lettr ko capital karte hain

name = "sumit"
print(name.capitalize())  # Output ???


# ==========================================
# REPLACE
# ==========================================

# isme ham string ko replace karte hain

# maan lo maine variable main sumit naam ka data save kiya hain
# aur ab mujhe use mangesh se replace karna hai to

# kya main mere pure code main wo variable dhundta baithu

# waise nahi

# iske liye ham replace ka use karte hani

# example ke saath samjte hain

# example.

name = "Sumit"
print(name.replace("Sumit", "Mangesh"))  # Output ???


# ==========================================
# FIND
# ==========================================

# soch tere code hain 1000 - 2000 linesh ka

# aur agar tu bhul gaya tune varible main kya add kiya hai

# to tu pura code to nahi dekhega

# to is liye find ka use hota hain

# example ke sath samjte hain

text = "I Love Python"
print(text.find("Python"))  # Output ???


# ==========================================
# CHECK WORD EXIST OR NOT
# ==========================================

# iska output "true" ya "false" main atta hain

# samaj tu bhul gaya code karte karte ke tune string main jo tuze add karna tha wo add kiya hain ya nahi

# to bass is check karne keliya use hota hain

# example.

text = "I Love Python"
print("Python" in text)  # Output ???

text = "I hate you"
print("love" in text)  # Output ???

# ye dono quetion ko alag alag se chala ke dekh okay fir tuze samaj main aayega

# dekh bhaii aaj jo bhi hmm padh rahe hai wo bass aise he hain

# extra koi explaination nahi hain

# ky kaise matt puchhh bass practice kar le


# ==========================================
# STRING SLICING
# ==========================================

# abb hoga thod intresting part chale

# ismain maja aayega

# aurr haa main bol raha hu bass use samaj

# maan lo

name = "sumit"

# aur mujhe ismai bass "mi" print karna ho to kaise kare

# ya starting ke words ya last words print karne ho

# ab jaise tuze pata hain hamne indexing pada hain

# ab uska use hoga yaha pe

# example.

name = "rohan"

# R O H A N
# 0 1 2 3 4

# ab samaj ja muje "oha" print karna hain

# chal bata ta hu kais kare

name = "rohan"
print(name[1:4])  # Output ???

# ab tu socheja "4" hain wo to "N" ko represent kar raha hain

# to hamne 4 lekha hai aur hame uske aage vaala no. mila

# exactly main wahi batane ke koshish kar raha hu

# aur example ke saath samajte hain

name = "sumit"
print(name[0:4])  # Output ???

# ab dekh maine yaha pe "[3: ]" space diya hai colon ke baad

# iska matlab hain last tak print hoga

# agar starting main space hain to starting se print hoga

# example.

name = "mangesh"
print(name[3:])  # Output ???

name = "aavishkar"
print(name[:6])  # Output ???


# ==========================================
# USER INPUT + STRING
# ==========================================

# bass kuch nahi hai easy hain

# example.

name = input("Enter Your Name : ")
print("Welcome", name)  # Output ???

# to abb isme jo

# name = input("Enter Your Name : ")

# enter your name hai wo user input hain

# yaha pe user input daalta hai

# aur jo "welcome" hai wo string hain


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1)

name = "Python"
print(name[0])

# 2)

name = "Python"
print(name[-1])

# 3)

name = "Python"
print(len(name))

# 4)

print("Hi" * 3)

# 5)

text = "I Love Python"
print("Python" in text)


# ==========================================
# MINI PROJECT
# ==========================================

# 1)

name = input("Enter Your Name : ")

print("Hello", name)
print("Length =", len(name))

# 2)

name = input("Enter Your Name : ")

print(name.upper())
print(name.lower())


# ==========================================
# END OF DAY 7
# ==========================================

# bass khatam day 7 to bolo bhai log kaise tha hamar aaj ke lecture

# to milte hai DAY 8 main

# tab tak ke liye

# jai hind
# jai bharat

# love you bhaiii log

# String Python mein text data ko represent karta hai,
# aur hamesha quotes ke andar likha jata hai.