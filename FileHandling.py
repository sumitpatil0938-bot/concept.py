# ==========================================
#           DAY 21 FILE HANDLING
# ==========================================

# welcom back to day 21 , to kaise ho aaj hai hamar day 21 to aaj ham pdane ja rahe hai 
# file handling ko detail main , to chalo shuru karte hain bina kisi time pass kiya 
# aur ha acche se detail main samjte hai 

# abhi tak ham data varibles main store kar rahethe barabr.
name = "sumit"
age = 21

# pr problem kya hai ?
# jab program band ho jayega to varible ka data bhi gayab ho jayega .

# example.
name = "sumit"
print(name) # // Output ???

# ab program close .
# phir dobara run karo.
# fir se value likni padegi.

# to iske liye solution hain ,
# data ko file main save karo , ha kar sakte hai kaise wo mai batata hu , dhya se dekh aur samaj aur practice kar.
# jaise koi bhi file ho sakte hai 
# file ke andar data permantaly save ho jayega 
# isko ham file handling bol te hai 


# ==========================================
# FILE HANDALING 
# ==========================================
# --> python ki help se file banana , padhna , likhna aur update karna isee ham file handaling bolte hai .


# ==========================================
# FILE OPEN KARNA 
# ==========================================
# bahi sun python mai file open karne ke liye ham "open()" function ka use karte hai.

# syantax: file = open("Filename.txt" , "mode")
# example.
file = open("varible.py" , "r")


# ==========================================
# FILE MODE
# ==========================================
# Sabse important mode hote hai
# 1) Read Mode (r) --> File read karne ke liye.
# 2) Write Mode (w) --> File main data likhne ke liye.
# 3) Append Mode(a) --> File ke end mein data add karne ke liye.


# 1) READ MODE
# example.
# maan lo file mein likha hai
# hello sumit
# welcome to python 

# Code --> file = open("student.txt" , "r")
#          data = file.read()
#          print(data) # // Output ???

# read() kya karta hai ? --> puri file ko read karta hai.


# 2) WRITE MODE
# example.
# Code --> file = open("student.txt" , "w")
#          file.write("Hellow Sumit")
#          file.close

# ab file main save hoga "Hello Sumit"

# IMPORTANT --> write mode purana data delete kar deta hai.

# example.
# file main pehle se kuch hai to write mode wo pehle waala data delet kar dega aur 
# jo hamne new data add kiya hai use add kar dega 


# 3) APPEND MODE
# ye use karte hain ham most of time kyu ki ,
# purana vaal data delet nahi karta , usmai new data add kar deta hai.
# exmaple.
# file mai --> Hello
# Code --> file = open("student.txt" , "a")
#          file.write("Sumit")
# ab file main save hoga "Hello Sumit"

# Difference = Write mode "w" --> purana data delete karta hai
#              Append mode "a" --> purana data aur new data save rakhta hai.

# ==========================================
# FILE CLOSE KARNA 
# ==========================================
# example.
# Code --> file = open("student.txt , "r")
#          print(file.read())
#          file.close()

# close kyu use karte hai ? --> kaam khatam hone ke baad file band karne ke liye.



# ==========================================
# READLINE()
# ==========================================
# Sirf ek line read karta hai.
# example.
# File mai --> python
#              java
#              c++
# Code --> file = open("student.txt" , "r")
#          print(file.readline())
#          # // Output ???


# ==========================================
# READLINES()
# ==========================================
# Saari lines list ke form main deta hai.
# example.
# Code --> file = open("student.txt , "r")
#          print(file.readlines())
#          # // Output ???


# ==========================================
# WITH OPEN()
# ==========================================
# ye modern aur best method hai.
# example.
# Code --> with open("student.txt" , "r") as file:
#               print(file.read())

# iska fayda ? --> automatically file close ho jati hai.
# hame --> file.close() likhne ke zarurat nahi hai.


# ==========================================
# FILE EXIT KARTI HAI YA NAHI ?
# ==========================================
# example.
# Code --> try:
#              file = open("student.txt" , "r")
#              print(file.read())
#          except FileNotFoundError:
#               print("File Not Found")
# Agar file nahi hogi to --> "File Not Found" print hoga 
# program crash nahi hoga iss se okay


# ==========================================
# REAL LIFE EXAMPLE
# ==========================================
# student data save karne ke liye 
# Code --> name = input("Enter name : ")
#          file = open("Student.txt" , "a")
#          file.write(name + "\n")
#          file.close()

# input --> kuch bhi do 
# file --> save hoga 

# fir dubara run:
# input --> alag dalo
# file --> save hoga 
# 
# aur purana bhi save rahega wo delet nahi hoga ,
# kyu ki hamne append ka use kiya hai na ki write ka , okay


# ==========================================
# FLOW OF FILE HANDLING
# ==========================================

# Step 1
# file open --> open()

# Step 2
# read/write/append
# read()
# write()

# Step 3
# close 
# close()


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1) kya save hoga ?
file = open("demo.txt", "w")
file.write("Hello")
file.close()

# 2) kya hoga ?
file = open("demo.txt", "a")
file.write(" Python")
file.close()

# 3) // Output ???
file = open("demo.txt", "r")
print(file.read())

# 4) ye kis method se file open kar raha hai ?
with open("demo.txt", "r") as file:
    print(file.read())

# 5) ye kya karega ?
file = open("demo.txt", "r")
print(file.readline())


# ==========================================
# MINI PROJECT
# ==========================================
# Student record saver 
name = input("Enter Name : ")
age = input("Enter Age : ")

with open("student.txt","a") as file:
    file.write("Name : " + name + "/n")
    file.write("Age : " + age + "/n")
print("Data Saved Successfully")


# to finally aaj hamar day 21 khatam , to aaj ke lecture min code hai pr jayda nahi to 
# abse tuze practice karna chalu karne padege kyu aage se aise he lectures hone vaale hai
# to tuze samjna padega aur khudse karna padega 
# to milte hai day 22 main kisi new topic ke saath tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳












