# ==========================================
#          DAY 39 WEB SCRAPING 
# ==========================================
# To kya haal chal bhai log firse swagat hainday 39 main.
# aaj ham python ka ek bahut hi intresting topic padhne wale hai.
# iska matlab hai..
# web scraping 
# agar tum kabhi sochte ho ki
# amazon ke products ka data kaise nikalne ?
# flipkart ki price automatically kaise read kare ?
# news website ki headline kaise collcet kare ?
# cricket score website se data kaise laaye ?
# to iska answer hai.
# web scraping.
# aaj ham ise bilkul basics se samjhenge.
# to bina kisi time pass kiye shuru karte hai.


# ==========================================
# WEB SCRAPING ???
# ==========================================
# simple language me --> website se automitacally data collect karna.
# normally :
# 1) browser open karo
# 2) website open karte ho
# 3) data read karte ho 
# 4) copy karte ho
# 5) pase karte ho

# ye sab manually hota hai.
# lekin ham to python padh rahe na 
# to hamm
# python se ye sab automatically kar sakte hai.
# simple defination yaad rakho
# WEB SCRAPING : Python ki help se website se automatically data nikalna.

# real life example.
# socho:
# Roz tum amazon par jaakar
# iphone ki price check karte ho
# manual process
# -> Open browse -> Search iphone -> Price dekho -> Browser band
# Ab socho :
# python ye kaam jhar roz kahud kare.
# aur agar price kam ho jaye.
# to tumhe message bhej de.
# ye hi web scraping hai.

# USE :
# * News Headlines collect karna
# * Weather Data lena
# * Stock Market Data
# * Product Price Tracking
# * Sports Scores
# * Job Listings
# * Research
# * Data Collection


# ==========================================
# WEB SCRAPING KE LIYE KYA CHAHIYE ??
# ==========================================
# mostly 2 libraries use hote hai.

# --> requests
# website ka html download karta hai.

# --> BeautifulSoup
# html ko read karta hai.


# ==========================================
# INSTALL KARNA 
# ==========================================
# terminal me
# --> pip install requests
# --> pip install beautifulsoup4

# IMOPRT :
# --> import requests
# --> from bs4 import BeautifulSoup4


# REQUESTS ??? 
# --> socho :
# tum website ko bol rahe ho.
# --> hello Website.
#     mujhe apne page bhejo.
# website jawab me HTML bhej sati hai.
# ye kaam
# --> requests
# karta hai.


# ==========================================
# PEHLA REQUEST
# ==========================================
import requests
response = requests.get("https://example.com")
print(response.status_code)
# // Output ???


# ==========================================
# STATUS CODE KYA HJOTA HAI ??
# ==========================================
# website ka reply.
# sabse common.
# --> 200
# matlab.
# Everything OK.

# --> 404 = page nahi mila.
# --> 500 = Website erro


# ==========================================
# HTMLA KYA HOTA HAI ?
# ==========================================
# Website ka original code.
# example.
# --> <h1>Hello</h1>
#     <p>Welcome</p>
# browser ise beautiful website bana deta hai.
# python ise text ke form me dekhta hai.


# ==========================================
# WEBSITE KA HTML DEKHNA
# ==========================================
import requests
response = requests.get("https://example.com")
print(response.text)
# // Output ???
# bahut bada HTML code.


# ==========================================
# BEAUTIFULSOUP KYA HAI ??
# ==========================================
# HTML ko samjhne wali library.
# socho.
# HTML ek jungle hai
# beautifulsoup guide hai.
# wo tumhe exactly batata hai.
# Heading kidhar hai
# Paragraph kidhar hai
# Image kidhar hai
# Title kidhar hai


# ==========================================
# BEAUTIFULSOUP OBJECT
# ==========================================
import requests
from bs4 import BeautifulSoup
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text,"html.parser")
# yaha pe (html.parser) --> html ko prase karta hai.


# ==========================================
# WEBSITE KA TITLE
# ==========================================
# --> print(soup.title)
# // Output ???
# --> <title>Example Domain</title>

# Sirf Text
# --> print(soup.title.text)
# // Output ???
# example domain

# First Heading :
# --> print(soup.h1.text)
# // Output ???
# example domain

# First Paragraph :
# --> print(soup.p.text)
# // Output ???
# Website ka pehla paragraph.


# ==========================================
# COMPLETE EXAMPLE
# ==========================================
import requests
from bs4 import BeautifulSoup
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text,"html.parser")
print("Title :",soup.title.text)
print("Heading :",soup.h1.text)
print("Paragraph :",soup.p.text)


# ==========================================
# HTML INSPECT KYA HOTA HAI ?
# ==========================================
# har website ka structure alag hota hai.
# browser me.
# right click -> inspect -> html dikhai deta hai.
# waha se pata chalta hai ki Title,Heading,Price,Image
# kis tag ke andar hai.


# ==========================================
# IMPORTANT NOTE
# ==========================================
# har website scraping allow nahi karti.
# kuch website Robots.txt
# rules aur terms of service
# follow karne padte hain.
# isliye hamesha legal aur ethical scriping karo


# ==========================================
# REAL LIFE USE
# ==========================================
# web scraping ka use hota hai.
# - Price tracker
# - News collector
# - Job portal
# - Data analysis
# - Market research
# - Cybersecurity intelligence
# - Research project


# ==========================================
# PRACTICE QUESTION
# ==========================================

# 1) Web Scraping kya hota hai ??

# 2) Website download karne ke liye kaunsi library use hoti hai ??

# 3) HTML read karne ke liye kaunsi library use hoti hai ??

# 4) Status code 200 ka matlab kya hai ??

# 5) Website ka title kaise print karoge ??


# ==========================================
# MINI PROJECT
# ==========================================
import requests
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print("Website Title :",soup.title.text)
print("Heading :",soup.h1.text)
print("Paragraph :",soup.p.text)


# Web Scraping = Python ki help se Website se automatically data nikalna.
# import requests
# from bs4 import BeautifulSoup
# requests.get()
# response.text
# response.status_code
# BeautifulSoup()
# soup.title.text
# soup.h1.text
# soup.p.text

# to finally aaj hamar day 39 complete hua
# aaj tumne python ki help se website se data nikalna seekha start kiya
# ye skill data science,automation aur cybersecurity me bahut kaam aati hai.
# lekin yaad rakhna,
# har website scrap karna allowed nahi hota.
# hamesha website ke rules aur terms of service ka respect karna.
# alge mission me aur advanced scraping techniques seekhenge
# aur ha congrats kal hamare series ka final day 40 hone vaala hai
# iska matlab ye nahi ke python khatam hua 
# python to aur bhi ahi 
# pr ham scraping tak he karte hai
# dekhte hai , aur ha hame day 40 tak to pad liye pr 
# iska matlab ye nahi ke hamara ho gaya 
# hame project bhi karne hai.
# okay 
# to milte kal day 40 main kisi new topic ke saath tab tak ke liye 
# JAI HIND🇮🇳
# JAI BHARAT🇮🇳