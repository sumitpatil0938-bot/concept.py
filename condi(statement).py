# ==========================================
#       DAY 13 CONDITIONAL STATEMENT
# ==========================================

# to kya haal chal bhai log firse swagat hai day 13 main to aaj ka hamar topic hain conditinal statement in python kya hote hote ,
# ise ham pure basics se padhenge aurr aaram aaram se samjenge example ke saath jaise ham daily karte hai bass waise he
# to bina kisis time pass kiye shuru karte hai day 13 ko


# CONDITIONAL STATEMENT

# CONDITIONAL STATEMENT --> iska matlab ye condition ke hissab se decision leta hai.
# abhi tak ham code likh rahe the aure use print kar rahe the jiska output direct mil rha tha , pr ab conditional statemet se python ko condition ke
# hissab se chalna padega ,

# pata hain tu nahi samja hoga ye python theory pe nahi question solving pe chalta hai bhai log, tu jitne question solve karega utna tuje acche se samaj aayega ,
# example.

# soch agar mujhe aise program banana ho:
# * Age 18 se bade hai --> vote kar sakta hai
# * Age 18 se kam hai --> vote nahi kar sakta

# to isme python ko 2 condition mil gyi 1) vote kar sakte and 2) vote nahi kar sakte
# ise ham conditional statement bolte kyu ki ham python ko condition dete hai aur , fir wo user ke input ke hisaab se run hota hai,
# kaise mai samjata hu , time de aaram se ho jayega


# ==========================================
# IF STATEMENT
# ==========================================

# ye sabse basic aur imp conditional statement hai

# syntax .
# if condition:
#     code

# kuch ise tarah se likha jata hain , example se samja ta hu

# example.
age = 20

if age >= 18:
    print("you can vote") # // Output ???

# ab tu upar ka syntax dekh aur hamne jo code likha hai wo dekh ,
# isme age >= 18 ye condition de hai hamne python ko
# ab samja , nahi to chal ab dek dusra example

# example.
age = 14

if age >= 18:
    print("you can vote") # // Output ???

# kuch bhi print nahi hoga kyu ki , tu khud dekh na condition lag he nahi rahi hai ,
# 14 >= 18 kya 14 bada hai 18 se nahi to print nahi hoga , to iske liye to "you can't vote aana chiye na"???
# haa barabar hai tu wahi aayega pr ruk thoda wo bhi pdte hai


# ==========================================
# IF ELSE
# ==========================================
# jaise hamne upar padha agar condition false hui to " you can't vote " wahi pad rahe hai
# iske liye ham else condition ka use karenge

# example
age = 14

if age >= 18:
    print("you can vote")

else:
    print("you can't vote")  # // Output ???

# ab isme kya hoga pehle python user input dekhega aur fir use compare karega,
# 14 >= 18 , isme wo nahi aayega to false aayega
# agar 18 + hai to true "you can vote", nahi to else condition "you can't vote" run hoga samja


# ==========================================
# ELIF
# ==========================================
# soch agar jayda condition hain na ki 2 , 2 condition main if , else use karte the , pr ab 4,5,6 condition hai to kya karega to isliye ham "ELIF" ka use karte hai ,
# example ke saath samjte hai ,

# student ke marks ham divide karte hai 4 condition main

# Grade A marks >= 90
# Grade b marks >= 70
# Grade c marks >= 65
# Grade d marks >= 36

# aur last vaala fail

# ab ham iske liye elif condition ka use karenge

# example.
marks = 45

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 65:
    print("Grade C")

elif marks >= 36:
    print("Grade D")

else:
    print("Fail")  # // Output ???

# ab tu khud karke dekh aur ha marks change kr marks = 45 hai tu tere hisab se daal ke dek aur run kake output check kr , okay.
# 2 se jyada matlab multiple conditions hai to to ham elif ka use karte hain , aur last main else ka use karte hain .


# ==========================================
# INDENTATION
# ==========================================
# ye bohat important hai

# python main ham curly bracket{} use nahi karte dusre language jaise .
# yaha pe ham log space ka use karte hai
# aur space dena imp hota hain kab kaha pe varna kahi barr loop run hota rehata hai.

# example.
age = 14

if age >= 18:
    print("you can vote")

# indentation matlab ab tu dekh hamne print ko if condition ke andar likha hai
# kyu ki wo if ko run karega na ,
# to ab print ko hamne andar lika hai to starting main space hai usee ham indentation bolte hain
# hamne elif condition mai bhi use kiya hai , saare statement main use hoga , aur aage jake jab tu DSA padega na to usmi to bass kabhi kabhi wo indentation matlab spacing ke wajse error aate hain


# ==============================================
# PYTHON CONDITION KAISE CHECK KARTA HAI ????
# ==============================================

# python starting se check karta hain , aur jaha pe usko uski conditin mil jayegi bass waha stop ho jayega .
# example.
sumit = 20

if sumit >= 90:
    print("Excellent")

elif sumit >= 73:
    print("good")

else:
    print("Not bad")

# to ab isme kya hoga python 1st condition dekhega aur khud ko false bol dega ,
# to ab 2nd pe dekhega aur khud ko false bo dega
# to ab 3rd matlab else pe aayega aur sochega saala ye to dono main nahi aarha hai , to
# to yaha pe last condition hai else , to ise else mai daal dete hai, aise chalta hai
# soch agar main sumit ko 91 kar du to python use "if" pe rukayega aur true bolega aur print karega .


# ==========================================
# COMPAROISION OPERATORS
# ==========================================
# ye jo comparision operators hai wo condition banane ke liye use hote hai
# condition to hamne padh lye saare to ab ham
# condition ko banane vaale comparision operators padte hai

# ==   Equal To
# !=   Not Equal To
# >    Greater Than
# <    Less Than
# >=   Greater Than Equal To
# <=   Less Than Equal To

# example ke saath samjte hai kuch bhi nahi hai isme eassy hai , bass samaj ja thoda demak laga le mere bahi

# example.
num = 20

if num == 10:
    print("Correct")

elif num != 10:
    print("nice")

else:
    print("nothing")

# ab tu khud dek maine kya kiya
# fist pe nahi hua to 2 nd pe aagaya
# aur 2nd pe ruk gaya kyki hamne iska (not equal to "!=") ka use kiya aur output 20 diya aur conditin main 10 daala hai to
# ( 20 != 10 ) elif main tha islye wo print ho gaya


# ==========================================
# LOGICAL OPERATORS
# ==========================================
# ye logic lagne main use hota hai ,

# 3 types hai

# 1) AND
# 2) OR
# 3) NOT


# ===========
# 1) AND
# ===========
# iske liye dono condition true hone chaiye
# ek bhi false nahi hone chaiye

# example.
age = 25

if age >= 18 and age <= 60:
    print("Eligible") # // Output ???

# ab tu dekh yaha pe do condition hai to true aayega , agar ek bhi condition false hui to print nahi hoga
# python khud ko false bol dega


# ===========
# 2) OR
# ===========
# ek bhi condition true hui to chalega
# false hui to bhi kuch nahi hoga

age = 65

if age < 18 or age > 60:
    print("Special Category") # // Output ???


# ===========
# 3) NOT
# ===========
# true ko false aur false ko true bana dete hai
# ye thoda confusing hai pr samaj ja iski koi theory nahi hoti , example se he samjna padta hai

print(not True)   # // Output ??? -> False
print(not False)  # // Output ??? -> True

# example 1.
age = 20

print(age > 18)      # // Output ???
print(not age > 18)  # // Output ???

# 1st print ka output true aayega ,pr
# 2nd print ka output false aayega kuki hamne aage not laga diya

not 21 > 18

# hamne khud bola hain 21 18 se bada nahi hai to python use false bolega


# example 2.
age = 10

print(age > 18) # // Output ???
print(not age > 18) # // Output ???

# 2nd print ka output kya aata agar not nahi laga te , nahi lagate to false aata , pr
# hamne khud bola hai

not 10 > 18

# to false aane vaala that pr hamne khud statement diye hai ke 10 18 se bada nahi hai (not) to python hamre statement ko padega
# aur hame bola hai 10 18 bada nahi hai to python bolega ha sahi bola hai tune to islaye python hamar sunta hai aur true deta hai kyu i hamne barobar bola hain na
# 10 18 se bada nahi hai , aur ye batane ke liye ham "not" ka use karte hai


# example 3.
logged_in = False

if not logged_in:
    print("Please Login") # // Output ???


# ==========================================
# NESTED IF
# ==========================================
# kuch nahi iska matlab hai if ke andar aur if ka use

# example.
age = 22

if age >= 18:

    if age >= 21:
        print("jai sumit") # // Output ???

# abhi nahi pr aaram aaram se sekh jayege use case , kaise karte hain ,


# ==========================================
# USER INPUT + CONDITIONAL STATEMENT
# ==========================================
# ab user inuput aur condition combine karte hain

# example.
age = int(input("Enter Age : "))

if age >= 18:
    print("You Can Vote")

else:
    print("You Cannot Vote") # // Output ???

# deekh ketina mushkil tha 😅


# ==========================================
# PRACTICE QUESTIONS
# ==========================================
# 1)
age = 20

if age >= 18:
    print("Adult") # // Output ???

# 2)
num = 10

if num == 15:
    print("matched")

else:
    print("Not matched") # // Output ???

# 3)
marks = int(input("Enter marks :"))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

else:
    print("Grade C") # // Output ???

# 4)
num = int(input("Enter number : "))

if num %2 == 0:
    print("even")

else:
    print("odd") # // Output ???

# 5)
name = input("Enter your name : ")

if name == sumit:
    print("correct")

elif name != sumit:
    print("Not me , its you")

else:
    print("Fail") # // Output ???



# to finalyy aaj hamar day 13 khatam , ab yaha se aage tak theory nahi hogi bass example he example honge , fir bhi main
# samjne ke try karung , aur tu bhi khud se karte ja thoda thoda aur demak bhi laga te ja aur daily practice ,
# to chal milte day 14 mai new tpoic ke saath tab tak ke liye

# jai hind
# jai bharat