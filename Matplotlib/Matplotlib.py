# ==========================================
#        DAY 38 MATPLOTLIB BASICS
# ==========================================

# to kya haal chal bhi log firse swagatr hai day 38 main
# matplotlib is new topic ke saath 
# ab tak humne numpy se numbers ko handle karna aur 
# pandas se table data ko handle karna seekha.
# lekin agar kisi ko data ko samjhana ho to sirf numbers dekhkar
# samjhna mushkil hota hai.
# isliye ham graph banate hai.
# matplotlib hame python me graph aur charts banana sikhata hai.
# aaj ham ise bilkul basics se samjhenge.
# to bina kisi time pass kiye shuru karte hain.


# ==========================================
# MATPLOTLIB KYA HOTA HAI ??
# ==========================================
# simple language me.
# matplotlib ek python library hai.
# ye graph aur charts banane ke liye use hota hai.
# simple 
# MATPLOTLIB = python library jo data ko graph ke form me dikhati hai.

# socho:
# agar mere pass ye kuch marks hain.
# marks = [75,80,90,78,56]
# to list dekhkar samajhna mushkil hai.
# lekin agar graph bana diya.
# to ek second me samajh aa jayega.
# isliye use karte hain.

# Real life example:
# socho ek companu ke sales.
# jan -> 10 lakh
# feb -> 15 lakh
# mar -> 20 lakh
# apr -> 18 lakh
# ye agar graph me dikhaya jaye.
# to turant pata chal jayega.
# sales bad rahi hai ya kam ho rahi hai.


# ==========================================
# MATPLOTLIB INSTALLATION
# ==========================================
# apne laptop ke terminal main 
# --> pip install matplotlib
# run karo aur run ho jaye to use baad main vs code
# ya aap jo bhi use kar rahe ho usmain import karo.

# import karne ke liye kuvh nahi bass
# code ke starting main 
# --> import matplotlib.pyplot as plt 
# likho bass ho gaya import 
# agar nahi samjha to youtube pe video dekh lo 

# yaha 
# --> matplotlib.pyplot 
# original module hai.
# Aur
# -->plt
# shortcut naam hai
# almost sab programmer yehi use karte hain.


# ==========================================
# LINE GRAPH
# ==========================================
# example.
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.show()
# // Output ??? 

# ek simple line graph run hua hoga 
# bahi coding starting main easy lagte hai
# baad main matlab kuch dino baad bohat hate hone lagta hai coding se
# pr agar tumne us time ya us phase main khud ko sambhal liye 
# aur fir bhi apne padhai continue rakhi
# to tume apne aap sare concept samj main aayenge aurr
# tume pata bhi chalega ke tumai kab aur kaise coding se lagav ho jayega
# so back to topic

# to kaise run hua ??
# Step by Step
# --> x (horizontal axis)
# --> y (Vertical axis)
# --> plt.plot() (Graph banaya)
# --> plt.show() Green scree par dikha diya

# ab ye samjne ke koi jarurat to nahi hai na.
# X Axis & Y Axis kya hota hai.


# ==========================================
# TITLE ADD KARNA
# ==========================================
# example.
# --> plt.title("graph title")
# agar graph ko title dena ho to apne code main ye 
# code daalo 
# aur output check karna 
# tumhare graph ke upar title add ho jayega 

# X Label :
# agar X(Horizontal Axis) ko kuch naam dena ho to 
# --> plt.xlable("___") 
# jo naam dena hai wo likh do 

# Y Label :
# agar Y(Vertical Axis) ko kuch naam dena ho to 
# --> plt.ylable("___")
# jo naam dena hai wo likh do 

# LINE COLOUR :
# example.
# --> plt.plot(x,y,colour ="_")
# colour change ho jayega graph line ka 

# LINE STYLE :
# example.
# --> plt.plot(x,y,linestyle="==")
# graph ke line ka style change kar dega

# MARKER
# example.
# --> plt.plot(subject,marks,marker="__")
# har ponit pr circle ho jayega 

# GRID
# graph main grid laane ke liye.
# --> plt.grid()

# example.
import matplotlib.pyplot as plt
subject = ["Math","Science","English","History"]
marks = [35,38,29,40]
plt.plot(subject,marks)
plt.title("My Marks")
plt.plot(subject,marks,color="red")
plt.plot(subject,marks,linestyle="--")
plt.plot(subject,marks,marker="p")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.show()


# ==========================================
# BAR GRAPH
# ==========================================
# example.
import matplotlib.pyplot as plt
students = ["sumit","mangesh","sahil"]
marks = [20,50,10]
plt.bar(students,marks)
plt.show()
# // Output ???


# ==========================================
# PIE CHART
# ==========================================
# example.
import matplotlib.pyplot as plt
marks = [20,50,10]
students = ["sumit","mangesh","sahil"]
plt.pie(marks,labels=students)
plt.show()
# // Output ???


# ==========================================
# HISTOGRAM
# ==========================================
# Data ka distribution dikhata hai.
# example.
import matplotlib.pyplot as plt
marks = [60,70,75,80,90,95,85]
plt.hist(marks)
plt.show()
# // Output ???


# ==========================================
# TO SAVE GRAPH INTO IMAGE(PNG) FORMAT
# ==========================================
# graph ko image ke form me save karna.
# --> plt.savefig("__")
# title apne man se add karo
# ye current folde main graph.png bana dega


# ==========================================
# REAL LIFE USE
# ==========================================
# Matplotlib ka use hota hai.
# - data science
# - Machine learning
# - AI
# - Sales report
# - banking
# - Healthcare
# - Weather report
# - Stock market
# - Research


# ==========================================
# PRACTICE TIME BUDDY
# ==========================================

# 1) Matplotlib import karne ke liye kya likhenge ?

# 2) Graph screen par dikhane ke liye konsa function use hota hai ?

# 3) Title add karne ke liye konsa function use hota hai ?

# 4) Bar Graph banane ke liye konsa function use hota hai ?

# 5) Pie Chart banane ke liye konsa function use hota hai ?


# ==========================================
# MINI PROJECT
# ==========================================
import matplotlib.pyplot as plt
subjects = ["Math","Science","English","Python"]
marks = [88,92,85,98]
plt.bar(subjects,marks)
plt.title("My Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid()
plt.show()
# // Output ???


# Matplotlib = Python Library jo Data ko Graph ke form me dikhati hai.

# import matplotlib.pyplot as plt
# plt.plot()
# plt.show()
# plt.title()
# plt.xlabel()
# plt.ylabel()
# plt.bar()
# plt.pie()
# plt.hist()
# plt.grid()
# plt.savefig()

# To finally aaj hamar day 38 khatam hua 
# ab tum python programmer se data visualization ki duniya 
# me enter kar chuke ho
# numpy data ko fst banata hai
# pandas data ko organize karta hai
# matplotlib us data ko graph ke form me dikhata hai.
# ye teen librariess(numpy+pandas+matploylib) data
# science ki foundation hain.
# inhe acche se practise karna.
# aurr ha main ye day 38 ke laga se folder bade hai 
# kuch error ke wajhe se ye matplotlib us main run nahi ho rahi thi 
# okay 
# to chalo milte hai day 39 main ek naye python concept ke saath 
# tab tak ke liye
# JAI HIND🇮🇳
# JAI BHARAT🇮🇳