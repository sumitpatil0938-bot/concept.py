# ==========================================
#         DAY 20 EXCEPTION HANDLING
# ==========================================

# wlecom back bhai log kaise ho , firse swagat hai day 20 mai
# to aaj ka hamar topic hain exception handling jise ham detail main samjte hai aaj ke lecture main
# easy topic hain bass samaj ja , aur practice kar , kyu ki aaj ka bohat assan topic hai.
# to chal shuru karte hai bina kisi timepass kiya 

# abhi tak jab ham code likhte the , agar code sahi hota tha to output aa jata tha 
# parr problem kab aati hai ??
# soch user se number lena hai aur hame bass input main 
# number chaiye aur user ne input main xyz daala to kya hoga ??
# ab python "ValueError" dedega
# ab kya hoga pura program wahi pe band ho jayega .
# to ise avoid karne ke liye ham exception handling ka use karte hain
# kaise wo ab main explain karung tu dhya se samj ja kar okay 

# Ye jo error aaya hai ise he ham Exception bolte hain

# EXCEPTION HANDLING
# --> program chal raha tha aur beech main koi error aa gaya jiske wajah se program ruk gaya 
#     us error ko exception bolte hain.


# ==========================================
# EXCEPTION HANDLING KYA HOTA HAI ?
# ==========================================
# --> Error aane ke baad bhi program ko crash hone se bachana.
#     matlab error aane ke baad bhi program run hoga aane vaale error ko handle karta hai , haa hota hai kaise wo main batung.


# ==========================================
# TRY & EXCEPT
# ==========================================
# bhai dhya se dekh ye important concept .
# synatx : try:
#               code
#          except:
#                  error handle

# example.
try:
    num = int(input("Enter number : "))
    print(num)
except:
    print("Invalid Input") # // Output ???

# agar user input main koi alphabate daalega to invalid output aayega 
# agar user input main koi number daalega to program ru ho jaye ga 

# to ab jo except vaala jo block hai wo error ko handle karta hain , samja tu ?
# agar nahi to ruk ja aage jake samaj me aayega 


# ==========================================
# FLOW SAMAJ
# ==========================================
# python pehle
# try: --> wala block chalata hai.
# agar sab sahi hai.
# try: --> complete ho jayega.

# agar error aaye to.
# except: --> wala block chalega.

# example.
try:
    print(10/0)
except:
    print("Error") # // Output ???

# ab jo error aaya hai use ham ZeroDivisionError bolte hai 
# kyu ?? error
# bhaii kisi bhi nuber ko 0 se didvide nahi kar sakte na isliye error aaya.

# example.
try:
    print(25/8)
except:
    print("Cannot Divide by zero") # // Output ???



# ==========================================
# SPECIFIC ERROR HANDLE 
# ==========================================
# abhi tak hamne [ except: ] likha 
# pr python main alag alag errors hote hain
# example.
# 1) ValueError 2) ZeroDivisionError 3) NameError 4) TypeError

# example.
try:
    num = int(input("Enter number : "))
    print(num)
except ValueError:
    print("Please Enter Number Only") # // Output ???

# user ne alphabate daale to bhi code run hoga pr ab try main error ayega aur except vaala block run hoga 
# aur user ne numbers daale to program run hoga pr try vaala block run hoga except tak nahi jayega 


# ==========================================
# MULTIPLE EXCEPT
# ==========================================
# soocho 2 alag alag error aa gaye to kaise handle kare .
# example.
try:
    num = int(input("Enter number : "))
    print(100/num)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Zero Not Allowed") # // Output ???

# CASE 1
# input --> xyz
# output --> invalid

# CASE 2 
# input --> 0
# output --> zero not allowed


# ==========================================
# ELSE
# ==========================================
# yaha pe else ka bhi use kar sakte hai.
# syntax : try:
#              code
#          except:
#                 error
#          else:
#               success

# example.
try:
    num = int(input("Enter number : "))
except ValueError:
    print("Invalid Number")
else:
    print("Success") # // Output ???

# ELSE tabhi chalta hai jab try block main error nahi aaye
# agar error aagay to except vaala run hoga 
# nahi to else vaala 


# ==========================================
# FINALLY
# ==========================================
# ye bohat important hai 
# finally hamesha chalta hai.
# error aaye ya na aaye.
# example 1.
try:
    print(10 / 0)
except:
    print("Error")
finally:
    print("Program End") # // Output ???

# example 2.
try:
    print(10 / 2)
except:
    print("Error")
finally:
    print("Program End") # // Output ???

# USE 
# file close karna .
# Database close karna .
# Cleanup work .
# Ye sab finally main hota hain .



# ==========================================
# COMPLETE FLOW
# ==========================================

# try: --> error aaya? yes --> except --> finally
#          error nahi aaya? --> else --> finally


# ==========================================
# REAL EXAMPLE
# ==========================================
try:
    num1 = int(input("Enter number : "))
    num2 = int(input("Enter number : "))
    print(num1//num2)
except ValueError:
    print("Invalid Number , Numbers allowed")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("calculation successful")
finally:
    print("program end")



# ==========================================
# PRACTICE QUESTION 
# ==========================================
# 1)
try:
    print(10/0)
except:
    print("error")

# 2)
try:
    num = int(input("enter number : "))
except ValueError:
    print("Wrong Input")

# 3)
try:
    print("Hello")
except:
    print("error")
else:
    print("Success")

# 4)
try:
    print(100/10)
except:
    print("Error")
finally:
    print("program end")

# 5)
try:
    print(100/0)
except ZeroDivisionError:
    print("Cannot Divide By Zero")



# ==========================================
# MINI PROJECT
# ==========================================
# Q) simple calculator ? bahi pehle khud se solve kar baad main agar error aa raha hai to code dekh le okay .
try:
    num1 = int(input("Enter number : "))
    num2 = int(input("Enter number : "))

    print("Addition : ",num1+num2)
    print("subtraction : ",num1-num2)
    print("multiplication : ",num1*num2)
    print("Division : ",num1//num2)
except ZeroDivisionError:
    print("Zero Not Allowed")
except ValueError:
    print("Only Numbers Allowed")
else:
    print("success")
finally:
    print("Program End")



# to finally aaj ka day 20 khatam to aaj hamne exception handling k detail main padha hai to ,
# practice kar le aasa hai , to milte hai agle lecture main day 21 main new topic ke saath 
# tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳




