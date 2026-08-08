# ==========================================
#            DAY 40 APIs BASICS
# ==========================================
# to kya hal chal bhai log kaise ho aaj hain hamara day 40
# aur aaj ka hamara topic hain APIs 
# aur ha easy topic hai 
# aur sabse importanat topic hai python ka 
# to bina kisi time pass kiye shuru karte hain.


# ==========================================
# APIs ?
# ==========================================
# APIs ( Application Programming Interface)
# ise tum middle man samaj sakte ho 
# example.
# tum restaurant me jaate ho.
# Tum -> Waiter -> Kitchen -> Waiter -> Tum
# tum directly kitchen me jakar food nahi banwate.
# tum waiter ko oreder dete ho.
# waiter kitchen ko order deta hai
# kitchen food banate hai.
# waiter tumhe food deta hai.
# APIs bhi kuch similar kaam karti hai

# your python program -> API -> server -> data -> your python program

# Defination --> Ek interface jiske through do software/applications ek
# dusre se communicate karte hain.


# Real Life Example :
# suppose tum weather app use kar rahe ho 
# tumne aap me dekha :
# --> pune
#     Temperature : 28°C
#     Humidity: 65%
#     Weather: Cloudy
# tum soch sakte ho:
# "ye data app ko mila kaha se??"
# app ke pass khud weather station nahi hai.
# app ek weather API ko request bhej ta hai.
# Weather App
#     ↓
# Weather API
#     ↓
# Weather Server
#     ↓
# Weather Data 
#     ↓
# Weather API
#     ↓
# Weather App


# ==========================================
# APIs MAIN REQUEST KYA HOTI HAI
# ==========================================
# Request ka mtalab:
# hum server se kuch maang rahe hai
# jaise restaurent me:
# --> Bhai ek pizza dena.
# API me:
# "Mujhe pune ka weather data chahiye."
# ye request hai


# ==========================================
# RESPONSE KYA HOTA HAI
# ==========================================
# Server request receive karta hai.
# data find karta hai.
# aur hum answer bhejte hai.
# is answer ko kheta hai --> Response

# REQUEST
# "Give me Pune weather"
#         ↓
#       SERVER
#         ↓
# RESPONSE
# "Temperature = 28°C"

# Request = hum kya maang rahe hain.
# Response = Server hume kya de raha hai.


# ==========================================
# API KA FLOW
# ==========================================
# ye flow samjna bahut importanta hai.
#         CLIENT
#           |
#           | REQUEST
#           ↓
#          API
#           |
#           ↓
#         SERVER
#           |
#           | RESPONSE
#           ↓
#          API
#           |
#           ↓
#         CLIENT
# yaha :
# Cilent = tumhara python program/app hai.


# ==========================================
# PYTHONSE API KO REQUEST KAISE BHEJTE HAIN?
# ==========================================
# yaha hum sirf apne purane friend ko use karenge.
# --> request
# day 39 me humne web scraping ke time request padha tha.
# APIs ke saath bhi requests bahut commonly use hota hai.


# ==========================================
# BASIC API REQUEST
# ==========================================
# example.
import requests
response = requests.get("https://api.example.com")
print(response)

# --> request.get() = server ko get request bhej raha hai.


# ==========================================
# GET KYA HOTA HAI
# ==========================================
# Get ka simple meaning: Data maangna.

# example.
# GET -> Mujhe data do.
# jaise : GET /users
# Matlab : Mujhe users ka data do 


# ==========================================
# API RESPONSE
# ==========================================
# API normally data return karti hai.
# Aajkal APIs me data commonly:
# JSON fromat main milta hai
# example.
{
    "name": "Sumit",
    "age": 20,
    "city": "Pune"
}
# ye JSON hai
# hamne ise day 34 me cob=vr kiya tha 


# ==========================================
# JSON RESPONSE PYTHON ME KAISE MILEGA ?
# ==========================================
# suppose API ne JSON return kiya
import requests
response = requests.get("https://api.example.com")
data = response.json()
print(data)

# yaha : response.json() = API ke json response ko python object me convert karne me help karta hai.


# ==========================================
# EK SIMPLE EXAMPLE
# ==========================================
# hum ek testing API use kar sakte hain:
# example.
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print(response.status_code)
data = response.json()
print(data)

# agar sub sahi ho raha ho to --> 200
# aur uske baad users ka data milega


# ==========================================
# STATUS CODE FIRSE
# ==========================================
# 200 -> success
# 404 -> Not found
# 500 -> Server error
# 401 -> Unauthorized
# 403 -> Forbidden (Access allowed nahi hai)


# ==========================================
# RESPONSE KO CHECK KARNA
# ==========================================
# Hum directly data lene ke bajay pehle check kar sakte hain:
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed")
# ye better approach hai.


# ==========================================
# SIRF EK USER KA DATA 
# ==========================================
# API me hum specific resource bhi maag sakte hai.
import requests
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
data = response.json()
print(data)
# yaha : /user/1
# ka matlab hai:
# user number 1 ka data.


# ==========================================
# SPECIFIC INFORMATION NIKALNA
# ==========================================
# suppose response me:
{
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "example@email.com"
}
# to :
print(data["name"])
# Output ???
# --> Leannne Graham
# Aur :
# --> print(data["email"])
# eamil dega.
# yaha tumhara dictonary concept bhi use ho raha hai.


# ==========================================
# API + JSON + DICTIONAY
# ==========================================
# ye connection bahut important hain.
# API
# ↓
# JSON
# ↓
# Python Dictionary
# ↓
# Data Access
# example.
# --> data["name"]


# ==========================================
# API KE HTTP METHODA
# ==========================================
# ab ek important concept.
# APIs me different HTTP methods hote hain.
# Basic level par ye yaad rakho.

# GET = Data lena (get -> give me data)
# POST = Naya data creat karta hai (post -> creat new data)
# --> New user creat karna
# PUT = Existing data ko upgrade karna
# PATCH = Existing data ka kuch parte update karta hai
# --> example. jise sirf emil change karna , ya naam change karne
# DELETE = Data delet karna. (delete -> remove data)


# ==========================================
# GET REQUEST KA PRACTICAL EXAMPLE
# ==========================================
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(user["name"])
else:
    print("Somethng went wrong")
# yaha hum : 
# 1) API ko request bhej rahe hai.
# 2) response receive kar rahe hai.
# 3) JSON ko python data me convert kar rahe hai.
# 4) Users ke naam print kar rahe hai.


# ==========================================
# API KO WEB SCRAPPING SE COMPARE KARO
# ==========================================
# ye difference important hai.

# Web Scrapping :
# Website -> HTML -> BeautifulSoup -> Data

# API :
# API -> JSON -> Python -> Data

# API available ho to generally structured data directly API se lena scrapping ke
# comparision me cleaner approch hota hai


# ==========================================
# API USE KAHA HOTE HAI.
# ==========================================
# har jagah use hota hai.
# Weather API
# Maps API
# Payment API
# Social Media API
# AI API
# Threat Intelligence API
# GitHub API


# ==========================================
# CYBERSECURITY MAIN API
# ==========================================
# ye hamarleiye espically imporatant hai.
# cybersecurity tools APIs ka use karke informations le sakti hai.
# example.
# Your Security Tool
#         ↓
# Threat Intelligence API
#         ↓
# IP / Domain Information
#         ↓
# Your Tool

# suppose tumhare pass koi suspicious Ip address hai.
# Tool API se information maang sakta hai:
# IP reputation
# Country
# ASN
# Threat score
# known malicious activity
# isliye APIs cybersecurity me bhi bahut important hain.


# ==========================================
# ORACTICE QUESTION 
# ==========================================
# 1) API ka full form kya hai?
# 2) API ka simple meaning kya hai?
# 3) Request kya hoti hai?
# 4) Response kya hota hai?
# 5) GET method kisliye use hota hai?
# 6) POST kisliye use hota hai?
# 7) JSON API response ko Python me access karne ke liye kya use kar sakte hain?
# 8) HTTP status code 200 ka kya meaning hai?
# 9) HTTP status code 404 ka kya meaning hai?
# 10) Web Scraping aur API me basic difference kya hai?


# ==========================================
# MINI PROJECT
# ==========================================
# Ab ek proper beginner project.
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
if response.status_code == 200:
    users = response.json()
    for user in users:
        print("Name :", user["sumit"])
        print("Username :", user["psumit25"])
        print("Email :", user["email@.com"])
        print("--------------------")
else:
    print("Failed to fetch data")

# is project me tumne combine kiya:
# Python
#    +
# Requests
#    +
# API
#    +
# JSON
#    +
# Dictionary
#    +
# Loop
#    =
# API Project

# so finally aaj hamar day 40 APIs complete hua 
# aurr ha acche se practice kar , kyu ki cybersecurity main bohat 
# important topic hai
# aur bass 1 day to go , fir hamare series khatam 
# waise to aaj he khatam hui hai 
# par day 41 main project kari hai aurr
# aage bhi hame project karne hai 
# to chal milte hai kisie new project ke saath 
# tak tak ke liye 
# JAI HIND🇮🇳
# JAI BHARAT🇮🇳