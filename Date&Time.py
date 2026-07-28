# ==========================================
#          DAY 33 DATE & TIME
# ==========================================
# to kya haal chal bhai log kaise ho aap
# welcome back to day 33 of our series ,
# to aaj ka hamar topic hai Date & time
# ye topic lagbag har python projet main use hota hai 
# aur cybersecurity main bhi imp hai 
# to shuru karte hai bina kisi time pass kiye.


# ==========================================
# DATE & TIME ???
# ==========================================
# simple language main
# python ko bhi 
# - date
# - time
# - yera
# - month
# - day 
# - hour
# - minute
# - second
# pata ho chahiye
# ye sab kaam python (datetime) module ki help se karta hai.


# ==========================================
# DATETIME MODULE
# ==========================================
# sabse pehle module import karte hai
# code --> from datetime import datetime
# orr
# code --> import datetime
# dono bhi use kar sakte hai
# mostly ham 1st vaala use karte hai


# ==========================================
# CURRENT DATE & TIME
# ==========================================
# example.
from datetime import datetime
now = datetime.now()
print(now)
# // Output ???
# bhii sun tumhara outpout alag higa kyu ki har second update hota hai
# time to kisi ke liye nahi rukta NA

# Step by Step 
from datetime import datetime
# module import hua.

# datetime.now()
# currwnt date aur time lekar aaya.

# now
# varible me store ho gaya

# python(now)
# screen par print ho gaya


# ==========================================
# SIRF DATE NIKALNA
# ==========================================
# example.
from datetime import datetime
today = datetime.now()
print(today.date())
# // Output ???

# ==========================================
# SIRF TIME NIKALNA
# ==========================================
# example.
from datetime import datetime
now = datetime.now()
print(now.time())
# // Output ???

# ==========================================
# YEAR
# ==========================================
# example.
from datetime import datetime
today = datetime.now()
print(today.year)
# // Output ???

# ==========================================
# MONTH
# ==========================================
# example.
from datetime import datetime
today = datetime.now()
print(today.month)
# // Output ???

# ==========================================
# DAY
# ==========================================
# example.
from datetime import datetime
today = datetime.now()
print(today.day)
# // Output ???

# ==========================================
# HOUR
# ==========================================
# example.
from datetime import datetime
now = datetime.now()
print(now.hour)
# // Output ???

# ==========================================
# MINUTE
# ==========================================
# example.
from datetime import datetime
now = datetime.now()
print(now.minute)
# // Output ???

# ==========================================
# SECOND
# ==========================================
# example.
from datetime import datetime
now = datetime.now()
print(now.second)
# // Output ???


# ==========================================
# COSTUME DATE & TIME
# ==========================================
# example.
from datetime import datetime
d = datetime(2026,7,27,10,30,15)
print(d)
# // Output ???

# ==========================================
# STRFTIME()
# ==========================================
# ab aata hai sabse important function.
# naam hai.
# strftime() --> ye data ko apne format me convert karta hai.
# example.
from datetime import datetime
today = datetime.now()
print(today.strftime("%d/%m/%y"))
# // Output ???
# ya pe kya hua ?? 
# normal output aata hai 2026-07-27
# ab check karo 
# matlab format change ho gaya 


# ==========================================
# COMMON FORMAT CODES
# ==========================================
# - %d -> Day
# - %m -> Month
# - %Y -> Full Year (2026)
# - %y -> Last 2 digit of year (26)
# - %H -> Hours (24 Hours)
# - %I -> Hours (12 Hours)
# - %M -> Minute
# - %S -> Second
# - %A -> Full day name
# - %B -> full month name

# example.
from datetime import datetime
today = datetime.now()
print(today.strftime("%A")) 
print(today.strftime("%B"))
# // Output ???


# ==========================================
# STRPTIME
# ==========================================
# ab iska ulta dekhta hain.
# ye strig ko data me convert karta hai.
# example.
from datetime import datetime
date = "27-07-2026"
d = datetime.strptime(date,"%d-%m-%y")
print(d)
# // Output ???


# ==========================================
# STRFTIME VS STRPTIME
# ==========================================
# ye interview main poochte hain.

# strftime() = Date -> satring
# matlab data ko apne format me badalta hai.

# strptime() = String -> Data
# matlab string ko data object me convert karta hai.

# simple trick
# strftime => format banata hai.
# strptime => parse karta hai.


# ==========================================
# DATE DIFFERENCE
# ==========================================
# example.
from datetime import datetime
d1 = datetime(2026,7,1)
d2 = datetime(2026,7,27)
print(d2-d1)
# // Output ???


# ==========================================
# REAL LIFE USE
# ==========================================
# date & time ka use hota hai
# - Attendence system
# - Banking
# - Instagram posts
# - Whatsapp messages
# - Login history
# - Cybersecurity logs
# - File creation data
# - OTP expiry
# - Password expiry
# - tickit booking
# har software main date and time hota he hai matlab lagbag hota hai


# ==========================================
# PRACTICE TIME
# ==========================================
# 1) 
from datetime import datetime
print(datetime.now())
# // Output ???

# 2)
from datetime import datetime
today = datetime.now()
print(today.year)
# // Output ???

# 3) 
from datetime import datetime
today = datetime.now()
print(today.strftime("%d/%m/%Y"))
# // Output ???

# 4) 
from datetime import datetime
date = "15-08-2026"
d = datetime.strptime(date,"%d-%m-%Y")
print(d)
# // Output ???

# 5) Python me Date & Time ke liye konsa module use hota hai??
# --> datetime module use hota hai.



# ==========================================
# MINI PROJECT
# ==========================================
# current date and time viewer
from datetime import datetime
now = datetime.now()
print("Current Date : ", now.strftime("%d/%m/%y"))
print("Current Time : ", now.strftime("%H:%M:%S"))
print("Day : ", now.strftime("%A"))
print("Month : ",now.strftime("%B"))
# // Output ???


# datetime.now() --> current date and time deta hai.
# strftime() --> data ko apne format me convert karta hai.
# strptime() --> string ko data object me conver karta hai.

# to finally aaj hamar day 33 date & time khatam 
# aaj ka topic assan tha aur bohat jayada important bhi tha
# kyu ki ye har jaga pe use hota hai
# aurr ha firse day one se start kar de revise karna 
# to chalo milte hai hamare agle lecture main kisi new topic 
# ke saath tab tak ke liye 
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳
