# ==========================================
#              DAY 14 LOOP
# ==========================================
# 
# to finally back to day 14 to aaj hamar topic hain loop , to aaj ham loop ko detail main padenge 
# to bina kisi time pass kiye shuru karte hain , aur ha dhyan se dekh theory nahi hai fir bhi main explain karung .


# Chal ab shuru hoga asli python ka khel , ab tujhe lagega ye kya hain kaise kiya ,
# kyu ki abse ham asli python shuru kar rahe hai , BE READY MY BOYS/GIRLS

# example ko dhya se dekha kr aur samja kr , aur khud run karke dekh liya kar taaki acche se samaj aaye okay .

# LOOP --> same kaam ko baar baar karna ise loop bolte hain.
# ek baat soch tujhe 5 baar tera naam print karna ho to tu kya karega ,
print("sumit")
print("sumit")
print("sumit")
print("sumit")
print("sumit")
# aise to nahi karega na , to iske liye ham loop ka use karte hain , aur abhi ham wahi topic padne ja rahe hai ,

# ==========================================
# TYPES OF LOOP
# ==========================================
# loop 2 types ke hote hain 
# 1) FOR LOOP 
# 2) WHILE LOOP 

# to chal ek-ek karke dono ko detail main padna shuru karte hai.


# ==========================================
# 1) FOR LOOP 
# ==========================================
# syntax: matlab patterna code likhne ka 
# for variable in sequence:
#     code 

# abhi kuch samaj nahi aayega , example dekh.
# example.
for i in range(5):
    print("mangesh") # // Output ???


# ==========================================
# RANGE() KYA HAI ????
# ==========================================
# ye bahut imp hai .
# range(5)
# python ise  kuch aise dekhta hai index ke form main 
# 0 1 2 3 4
# matlab 5 nahi aata , " LAST VALUE SE EK KAM " .
# example.
for i in range(6):
    print(i) # // Output ???
# jo range hamne dete hai ussee ek kam aata hai hamesha yaad rakhhh.


# ==========================================
# i KYA HAIN ????
# ==========================================
# i sirf ek variable hai 
# tu i ka naam change karke kuch bhi rakh sakta hai.
# example.
for sumit in range(4):
    print("mangesh") # // Output ???


# ==========================================
# RANGE(START,END)
# ==========================================
# ab soch tune range(3) daala hai pr tuze kahi se start karna ho aur khatam to kaise karege
# agar tu upar vaala karega to starting se shuru karega aur tune jo range de hai waha pe khatam ,
# agar tuze kahi bech main se start karna ho to kaise karega ?? is liye ham range(start,end) ka use karte hai
# example.
for i in range(3,7):
    print(i) # // Output ???
# lat vaala include nahi hota , tu run karke dekh 7 include nahi hua hoga , 6 pe he ruk jayega


# ==========================================
# RANGE(START,END,STEP)
# ==========================================
# ab tu start end to samj gaya ab step ko bhi samaj ja use taraha,
# step matlab , jo value hamne daali hain utne value ka jump leta hai .
# example.
for i in range(3,31,3):
    print(i) # // Output ???


# ==========================================
# LOOP WITH STRING
# ==========================================
# string bhi loop mai chal sakta hai
# example.
name = input("Enter name : ")
for i in name:
    print(i) # // Output ???
# python jo hai wo ek-ek word ko pakad pakad ke print karta hai,


# ==========================================
# LOOP WITH LIST
# ========================================== 
# list main bhi loop ka use hota hain, list main jaise indexing bass waise he 
# loop list ko indexing karta hain.
# example.
fruits = ["apple","mango","banana"]
for i in fruits:
    print(i) # // Output ???


# ==========================================
# 2) WHILE LOOP
# ==========================================
# ye jab tak condition true hai tab tak chalta rahega.
# syntax:
# while condition:
#      code
# example.
num = 1
while num <= 6:
    print(num)
    num = num + 1 # // Output ???


# ==========================================
# num = num + 1 kyu ???
# ==========================================
# ye bahut important hai 
# agar ye likha to loop band hoga , agar nahi likha to loop continue rahega aurr , band he nahi hoga ise 
# Infinite loop bolte hai. 
# ek kaam kr num = num + 1 mat likh aur print kar ,

# num = 8
# while num <= 9:
#     print(num) # // Output ???

# run karke dek kya hoga tu khud dekh.


# ==========================================
# BREAK 
# ==========================================
# loop ko beech main rook deta hai.
# example.
for i in range(10):
    if i == 5:
        break
    print(i)

# i == 5 ab ye jo 1 to 9 tak print kar raha tha to usee 5 tak he ruka dega ,
# kyu ki jab index 5 aayega tab python use , usi time break kr dega 


# ==========================================
# USER INPUT + LOOP 
# ==========================================
num = int(input("Enter number : "))
name = input("Enter : ")

for i in range(num):
    print(name)

# bhaii user input to main bohat pehle se padha raha hu ,
# ye to tujhe aata hoga na 


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1)
for i in range(5):
    print(i)

# 2) 
for i in range(1,6):
    print(i)

# 3) 
name = "python"
for i in name:
    print(i)

# 4) 
num = 1
while num <= 6:
    print(num)
    num = num + 1

# 5)
for sumit in range(15):
    if sumit == 13:
        break
    print(sumit)

# ==========================================
# MINI PROJECT 
# ==========================================
num = int(input("Enter Number : "))

for i in range(1,11):
    print(num * i)

# Table ka project hai ye 

# To finally aaj hamar day 14 khatam , to aaj hamne khatam kiya hai loop ko ,
# aajse ham asli python ko samjne vaale hain iski practice karte ja ,
# to milte hai day 15 min new topic ke saath , tab tak ke liye 
# jai hind
# jai bharat


# Loop = Repeat

# for loop = Fixed number of times

# while loop = Jab tak condition true

# break = Loop band

# continue = Current iteration skip

# range() = Numbers generate karta hai
