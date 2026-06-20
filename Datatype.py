# DATA TYPE DAY 3 

# DATA TYPE -> Data type ek aisa concept hai jisme hum ye define karte hai ki variable ke andar ka data kis type ka hai.
#              
# 
#  python ko pata hona chaiyae ki variable mein kis type ka data store hai taki python us data ke sath sahi operation perform kar sake.
# 
# types of data type


# 1] STRING -> String ek aisa data type hai jisme hum text store karte hai. 
#              String ko hum double ya single quote ke andar likhte hai.
# eg. name = "Sumit"  # double quote (" ")
#     name = 'Sumit'  # single quote (' ')
name = "Sumit"

print(name)
print(type(name))

#.  // output ( ? )

# 2] INTEGER -> Integer ek aisa data type hai jisme hum numbers store karte hai.
#              Integer ko hum bina quote ke likhte hai.
# eg.
age = 21

print(age)
print(type(age))

#. // output ( ? )

# 3] FLOAT -> float ek aisa data type hota hai jisme hum decimal valu store krte hai.
#              Float ko hum bina quote ke likhte hai.
# eg. 
price = 21.5

print(price)
print(type(price))

#. // output ( ? )

# 4] BOOLEAN -> Boolean ek aisa data type hota hai jisme hum TRUE ya FALSE value store krte hai.
#              Boolean ko hum bina quote ke likhte hai.
# eg.
is_student = True

print(is_student)
print(type(is_student))

#. // output ( ? )

# COLLECTION DATA TYPE -> Collection data type ek aisa data type hota hai jisme hum multiple values store krte hai.
#
# jais eg -> List , Tuple , Set , Dictionary
   
# 1] LIST -> mulitiple vale store karne ke liye list ka use karte hai. 
#            List ko hum square bracket [ ] ke andar likhte hai.

#Features

#✅ Ordered (sequence maintain hoti hai)

#✅ Changeable (modify kar sakte hain)

#✅ Duplicate values allow karta hai

# eg. 
shopping = ["Milk", "Bread", "Butter", "Eggs"]

print(shopping)

#. // output ( ? )

# 2] TUPLE -> Tuple bhi List ki tarah hota hai lekin ek baar create hone ke baad uski values change nahi kar sakte.
#             tuple ko hm round bracket ( ) mai likhte hai.
#Features

#✅ Ordered

#❌ Unchangeable (Immutable)

#✅ Duplicates Allowed

# eg. 
dob = (15, 8, 2003)

print(dob)

#. // output ( ? )

# IMP : "Tuple use karte hain jab data fixed ho."

# 3] SET -> isme duplicate values allow nahi karte.
#           set ko curly bracket {} mai likhte hai.
#Features

#❌ Order fixed nahi hota

#❌ Duplicates allowed nahi

#✅ Fast searching

# eg.
roll_numbers = {101, 102, 103, 103}

print(roll_numbers)

#. // output ( ? )

# iss question mai 103 do baar hai pr python ise ek he bar run krta hai.

# 4] DICTIONARY -> dictionary ek aisa data type hai jisme hum key:value pair store karte hai.
#                 dictionary ko curly bracket {} ke andar likhte hai.

#.     simple language samje to : Har value ka ek naam (key) hota hai.

#Maan lo ek student ka form hai:   Name  : Sumit
#                                  Age   : 21
#                                  City  : Mumbai       
#                                  
#                                  Yahan:
#                                           Name → Key
#                                           Sumit → Value
#                                           Age → Key
#                                           21 → Value
#                                           City → Key
#                                           Mumbai → Value

#Python mein ise Dictionary kehte hain.

# eg. 
student = {
    "name": "Sumit",
    "age": 21,
    "city": "Mumbai"
}

print(student)

#. // output ( ? )








# Dictionary ek collection hai jo data ko “Key : Value” pair mein store karti hai, jaise Name : Sumit, Age : 21, City : Mumbai. Isse data ko easily identify aur access kiya ja sakta hai. 


