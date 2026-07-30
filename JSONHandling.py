# ==========================================
#          DAY 34 JSON HANDLING
# ==========================================
# to kya haal chl bhi log kaise ho 
# welcome back to day 34 of JSON handling ,
# to aaj ka lecture amazing hone vaala hai
# asan hai pr confusing hai 
# aaj samjega pr confused hoga 
# aage aane vaale time main tu ise topic ke saath familier ho jaoge
# to shuru karte hai bina ksis time pass kiye 


# ==========================================
# JSON KYA HOTA HAI ??
# ==========================================
# JSON (Javascript Object Notation)
# naam javascript hai pr
# JSON sabhi language pr kaam karti hai.
# example : python, java, c++, PHP, Nodejs and etc...
# sabhi language main JSON ka use hota hai
# simple yaad rakho 
# --> JSON => Data store aur data transfer karne ka rk standard format hai.

# Real life example.
# socho tere college me student ki information save karni hai.
# jaise , name, age, city, course
# to ham ise JSON me aise likhte hain.
{
    "name" : "Sumit",
    "age" : 20,
    "city" : "pune"
}

# ye dikhne main same dictionary jaisa lag raha hai.
# aur ye baat bilkul sahi hai.
# python dictionary aur JSON ks structure almost same hota hai.


# ==========================================
# JSON DICTIONARY JAISE KYU DIKHTA HAI ???
# ==========================================
# python dictionary ->
student = {
    "name" : "mangesh",
    "age" : 20,
    "city" : "pune"
}
# JSON Dictionary ->
{
    "name" : "mangesh",
    "age" : 20,
    "city" : "pune"
}

# Difference sirf itna hai.
# Dictionary python object hai.
# JSON text format hai.
# ye line bohat imp hai 


# ==========================================
# JSON USE KYU KARTE HAI ???
# ==========================================
# socho :
# ek python program bana.
# Dusra java program bana.
# Ab python ko java ko data bhejna hai.
# python dictionary direct java nahi samjhega na .
# isliye ham JSON ka use karte hai.
# Matlab :
# python --> JSON --> Java

# jaise hamne upar padha tha sabhi language ko JSON samaj aati hai.


# ==========================================
# JSON MODULE
# ==========================================
# python main JSON use karne ke liye module import karte hai.
# --> import json
# ye module pura kaam karega


# ==========================================
# PYTHON OBJECT KO JSON ME BADALNA
# ==========================================
# iske liye
# --> jsson.dumbs()
# use karte hai
# example.
import json 
Student = {
    "sumit" : "sumit",
    "age" : 20,
    "city" : "pune"
}
result = json.dumps(Student)
print(result)
# // Output ???

# ye kya huaa ??
# step by step
# student --> dictionary tha
# json.dumbs(Student) --> Dictionary ko json string me convert kar diya
# print hua
# simple
# Dumps matlab:
# Dictionary -----> JSON String


# ==========================================
# JSON KO PYTHON ME BADALNE
# ==========================================
# iske liye
# --> json.loads()
# use karte hai
# example.
import json
data = '{"name":"sumit","age":20}'
student = json.loads(data)
print(student)
# // Output ???

# ye kya huaa ??
# step by step
# json string
# json.loads() --> ne usko dictionary bana diya
# ab ham dictionary ki tarah use kar sakte hain.
# example. --> print(student["name"])
# Loads matlab:
# JSON string -----> Dictionary
# trick to remember "Load JSON into python"


# ==========================================
# DUMPS VS LOADS
# ==========================================
# DUMPS
# Dictionary -----> JSON String

# LOADS
# JSON string -----> Dictionary


# ==========================================
# JSON FILE BANANA
# ==========================================
# abhi tak ham memory me kaam kar rahe the.
# ab file me save karte hain.
# example.
import json
student = {
    "name": "mangesh",
    "age" : 20
}
with open("student.json","w") as file:
    json.dump(student,file)

# ab isee run karke dekho iska output terminal main nahi aayega
# apne aap student.json ke file crest ho jayege aur us main save ho jayega


# ==========================================
# DUMP()
# ==========================================
# ye dictionary ko file me save karta hai.
# notice --> dump() & dumps()
# sam lag rahe hoge pr nahi hai
# DUMP: dump()
# Dictionary ---> JSON file
# DUMPS: dumps()
# Dictionary ---> JSON string


# ==========================================
# JSON FILE PADHNA
# ==========================================
import json
with open("student.json","r") as file:
    data = json.load(file)
print(data)


# ==========================================
# LOAD()
# ==========================================
# ye json file ko read karta hai.
# LOAD: load()
# JSON file ---> Dictionary
# LOADS: loads()
# JSON string ---> Dictionary


# ==========================================
# REAL LIFE USE
# ==========================================
# JSON ka use hota hai.
# - API
# - Instagram
# - Whatsapp
# - Facebok
# - Banking Apps
# - Amazon
# - Flipkart
# - Weather Apps
# - Cybersecurity Tools
# - Log Files

# Almost har jagah


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1) 
import json

student = {

    "name":"Amit"
}

print(json.dumps(student))

# // Output ???

# 2)
import json

data = '{"city":"Pune"}'

print(json.loads(data))

# // Output ???

# 3) Python me JSON module import karne ke liye kya likhenge ??

# 4) Dictionary ko JSON String me convert karne ke liye konsa function use hota hai ??

# 5) JSON String ko Dictionary me convert karne ke liye konsa function use hota hai ??


# ==========================================
# MINI PROJECT
# ==========================================
import json
student = {
    "class" : "2nd year",
    "course" : "computer science (CFIS)",
    "clg" : "D Y Patil university"
}
json_data = json.dumps(student)
print("JSON Data")
print(json_data)
python_data = json.loads(json_data)
print()
print("Python Dictionary")
print(python_data)


# JSON = Data Transfer aur Data Store karne ka Standard Format.
# dump()    → Dictionary → JSON File
# dumps()   → Dictionary → JSON String
# load()    → JSON File → Dictionary
# loads()   → JSON String → Dictionary

# To finally aaj hamara day 34 complete ho gaya 
# pehle ye 4 functions thode confusing lagenge, 
# lekin 2-3 baar practice karega to automatically yaad ho jayenge.
# aur haan, API aur Web Development start karte hi tujhe JSON har jagah dekhne ko milega.
# to milte hai day 35 main kisi new topic ke saath tab tak ke liye
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳