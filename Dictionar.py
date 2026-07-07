# ==========================================
#            DAY 12 DICTIONARY
# ==========================================


# INTRODUCTION

# to finally back guys aaj hain hamar day 12 ji main ham padne ja rahe hai dictionary
# ke baare main detail main , to kya hain dictionar uska use case etc. sab samjte hain aaj ke lectures main
# shuru karte hai bina time pass kiye kyu ki ye bhi chota topic hain , unta bada nahi aur easy bhi bohat hain


# WHY DICTIONARY ??

# abhi tak hamne list,tuple aur kal set padha hain to us mai ham kay karte hain dirct values store karte the okay , soch agr tuze kisi ke information store karne ho ,
# jaise ki name,age,city,school,and etc to list,tuple , aur set main nahi store kar sakte na
# age ham list tuple ya set main store karte hai to o kuch aisa aayega

list = ["sumit",21,"pusad"]
tuple = ("sumit",21,"pusad")
set =  {"sumit",21,"pusad"}

# ab agar to ise store karna bolta hain to tu pagal hain abhi tak tuze nahi samja kuch bhi tu fir se day 1 se start kr
# to mere bhai waise nahi hota hain , isliye ham dictionary padte hain ,

# example.

student = {
    "name": "Sumit",
    "age": 21,
    "city": "Pusad"
}

# ise dictionar bolte hain ise ham detail mai samjenge

# "name" -> Key hote hai
# "Sumit" -> Value hote hai

# "age" -> Key hote hai
# 21 -> Value hote hai

# "city" -> Key hote hai
# "pusad" -> Value hote hai



# MAKING OF DICTIONAR

# dictionary ko ham curly bracket"{ }" main likhte hai

student = {
    "name" : "sumit",
    "age" : 21,
    "city" : "pusad",
}

print(student) # // Output ???



# VALUES KO ACCESS KAISE KARTE HAIN ??

# ismi indexing nahi hoti yaad rakh ismain indexing nahi hoti

# example.

student = {
    "name": "Sumit",
    "age": 21
}

print(student[0])

# dictionar hamesha key se access hoti hai

# example.

student = {
    "name": "Sumit",
    "age": 21
}

print(student["name"]) # // Output ???
print(student["age"]) # // Output ???



# STORAGE IN DICTIONARY

# kuch bhi store kar sakte hai ,jo tuze lagta hin store hota hai wo sab kuch hota hai

# example.

dictionary = {
    "name ":"sumit",
    "age" : 21,
    "school": "JES",
    "marks": 56,
    "phn": 77760467
}



# CHANGE IN VALUE

# dictionary mutable hain hai , matlab changes ho sakte hain



# REPLACE

# ye dictionar main ke key ki values replace karti hain

# example.

student = {
    "name": "Sumit",
}

student["name"] = "Mangesh"

print(student) # // Output ???



# ADD VALUES

# ye new key and uski values add karta hain

student = {
    "name":"sumit",
}

student["city"] = "pusad"

print(student) # // Output ???



# REMOVE VALUE

# ye key and uski values remove karta hain
# uske liye ham pop() ka use karte hain

# example.

student = {
    "name":"sumit",
    "age": 21,
}

student.pop("age")

print(student) # // Output ???



# LINGTH OF DICTIONARY

# ye hame batata hai ke hamre dictionar ketni badi hai

# example.

student = {
    "name": "Sumit",
    "age": 21,
    "city": "Pune"
}

print(len(student)) # // Output ???



# KEYS

# sirf key deta hai dictionar main ke

student = {
    "name": "Sumit",
    "age": 21
}

print(student.keys()) # // Output ???



# VALUES

# ye values deta hai dictionar main ke

# example.

student = {
    "name": "Sumit",
    "age": 21
}

print(student.values()) # // Output ???



# ITEMS

# ye keys and uski values dono deta hain dictionary mai ke

# example.

student = {
    "name": "Sumit",
    "age": 21
}

print(student.items()) # // Output ???



# CHEAKING EXIST OR NOT

# ye check karta hain ke key ya values hamare dictionary main exist karta hain ya nahi.
# output hamesha boolean type mai aata hain , agar nahi pata to day 1 se shuru kar tu
# boolean matlab true ya false main atta hai

# example.

# 1)

student = {
    "name": "Sumit",
    "age": 21
}

print("name" in student) # // Output ???


# 2)

student = {
    "name": "Sumit",
    "age": 21
}

print("city" in student) # // Output ???



# ==========================================
#            PRACTICE QUESTION
# ==========================================

# 1)

student = {
    "name": "Sumit",
    "age": 21
}

print(student["name"]) # // Output ???


# 2)

student = {
    "name": "Sumit",
    "age": 21
}

print(student["age"]) # // Output ???


# 3)

student = {
    "name": "Sumit"
}

student["city"] = "Pune"

print(student) # // Output ???


# 4)

student = {
    "name": "Sumit",
    "age": 21
}

student.pop("age")

print(student) # // Output ???


# 5)

student = {
    "name": "Sumit",
    "age": 21,
    "city": "Pune"
}

print(len(student)) # // Output ???



# ==========================================
#                PROJRCT
# ==========================================

# usre input vaala project hain user se input lo aur use dictionary main daalo

name = input("Enter Name : ")
age = int(input("Enter Age : "))
city = input("Enter City : ")

student = {
    "name": name,
    "age": age,
    "city": city
}

print(student) # // Output ???



# ==========================================
#                END NOTES
# ==========================================

# to finally aaj hamar day 12 khatam , bola tha na assan hain aue bohat chote chote aur basics topic hain
# bass daily karte jaoo ho jayega assan hain hai
# to milte hai kal kisi new topic ke saath tab tak ke liye
# jai hind
# jai bharat

