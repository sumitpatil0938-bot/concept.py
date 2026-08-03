# ==========================================
#           DAY 37 PANDAS BASICS
# ==========================================
# to kya haal chal bhi log kaise hosab thik
# to aaj hai hamaer day 37 of python series
# aur aaj ham padhne ja rahe hain pandas ke baare main
# agar tum futur me data science , machine learning , artificial intelligence,
# data analysis ya analytics ki field me jana chahte ho.
# to pandas tumhare liye sabse important library hai.
# Numpy numbers ke liye famous hai.
# lekin pandas table aur data ko manage karne ke liye famous hai.
# aaj ham pandas ko bilkul basics se samjhenge.
# to bina kisi time pass kiye shuru karte hain.


# ==========================================
# PANDAS KYA HOTA HAI ?
# ==========================================
# simple language me.
# pandas ek python library hai.
# ye hamne
# - Table data
# - Excel Data
# - CSV Files
# - Database Data
# ko easily read , modify aur analyze karne me help karti hai.
# simple definition yaad rakh.
# Pandas = python library jo table data ko read, Analyze aur manage karne ke liye use hoti hai.


# ==========================================
# PANMDAS KA NAAM PANDAS HI KYU HAI ?
# ==========================================
# Bahut log sochte hain ki iska relation panda se hai.
# actually 
# pandas
# ka naam aaya hai
# --> panel data
# se 
# lekin aaj sab ise panda wali library hi bolte hai


# ==========================================
# PANDAS KI ZARURAT KYU PADI ??
# ==========================================
# python me list,dictionary,tuple,
# already the.
# fir pandas ki kya zarurat thi ??
# answer
# socho.
# Tumhare college me 
# 50 students
# 100 students
# 1000 students
# ya 
# 10 lakh students
# ka data hai.
# agar list me store karoge
student = {
    ["sumit",20,90],
    ["rahul",21,80],
    ["Amit",19,95]
}

# ye manage karna difficult ho jayega.
# isliye pandas use karte hain.


# ==========================================
# REAL LIFE EXAMPLE
# ==========================================
# suppose
# college ka student record.
# NAME         AGE        MARKS
# Sumit        20         90
# Rahul.       21         80
# Amit         19         95

# ye table exactly pandas handle karta hai.


# ==========================================
# PANDAS INSTALL KAISE KARE ??
# ==========================================
# terminal me.
# --> pip install pandas

# ==========================================
# IMPORT KAISE KARTE HAIN ??
# ==========================================
# example.
# --> import pandas as pd
# yaha --> pandas
# original library hai.
# aur
# --> pd
# shortcut naam hai.
# Almost har programmer isi shortcut ka use karta hai.


# ==========================================
# SERIES KYA HOTA HAI ??
# ==========================================
# pandas ka sabse basic object hai.
# series
# simple language me.
# series = single column data
# example.
import pandas as pd
marks = pd.series([70,80,90,95])
print(marks)
# // Output ???

# ye kaise chala ?? 
# step by step
# pd.series() -> list li -> usko series bana diya -> har value ke saath index automatically aa gaya


# ==========================================
# SERIES ME INDEX
# ==========================================
# example.
import pandas as pd
marks = pd.series([50,60,70])
print(marks[0])
# // Output ???

# ==========================================
# DATAFRAME KYA HOTA HAI ???
# ==========================================
# ye pandas ka sabse important concept hai.
# simple definition.
# Dataframe = rows aur columns wala table.
# ye excel sheet jaisa hota hai.


# ==========================================
# PEHLA DATAFRAME
# ==========================================
# example.
import pandas as pd
student = {
    "name":["sumit","rahul","amit"],
    "age":[20,21,19],
    "marks":[90,80,95]
}
df = pd.dataframe(student)
print(df)
# // Output ???

# ye kya hua ??
# dictionary gaya. -> pd.DataFrame() -> Dictionary ko table bana diya.
# simple.


# ==========================================
# COLUMN SELECT KARNA
# ==========================================
# --> print(df["Marks"])
# // Output ???

# ==========================================
# MULTIPLE COLUMNS
# ==========================================
# example.
# --> print(df[["name","Marks"]])
# // Output ???

# ==========================================
# ROW SELECT KARNA
# ==========================================
# example.
# --> print(df.loc[0])
# // Output ???

# ==========================================
# FIRST 5 ROWS
# ==========================================
# example.
# --> print(df.head())
# // Output ???
# head
# starting ki rows dikhata hai.

# ==========================================
# SHAPE
# ==========================================
# Rows aur columns batata hai.
# example.
# --> print(df.shape)
# // Output ???

# matlab 3 rows , 3 columns

# ==========================================
# COLUMNS
# ==========================================
# example.
# --> print(df.column())
# // Output ???

# ==========================================
# INFO()
# ==========================================
# Data ki information deta hai.
# example.
# --> print(df.info())
# // Output ???

# ye batata hai.
# - Kitni rows
# - kitne columns
# - Data type
# - Memory

# ==========================================
# DESCRIBE()
# ==========================================
# Numbers ka summary deta hai.
# example.
# ye batata hai.
# - mean
# - max
# - min
# - count 
# - standard Deviation


# ==========================================
# CSV FILE READ KARNA
# ==========================================
# ye pandas ka sabse famous feature hai.
# example.
import pandas as pd
df = pd.read_csv("student.csv")
print(df)
# // Output ???
# bas 
# ek line me pura CSV read ho gaya.


# ==========================================
# REAL LIFE USE ???
# ==========================================
# pandas ka use hota hai.
# - data science
# - machine learning
# - banking
# - finance
# - healthcare
# - cybersecurity logs
# - excel reports
# - sales analysis
# - weather analysis

# Almost har data project me pandas hota hi hota hai.


# ==========================================
# PRACTICE QUESTION
# ==========================================
# 1) 
import pandas as pd
data = pd.Series([10,20,30])
print(data)

# // Output ???

# 2) Pandas import karne ke liye kya likhenge ??

# 3) Series kya hoti hai ??

# 4) DataFrame kya hota hai ??

# 5) CSV File read karne ke liye konsa function use hota hai ??


# ==========================================
# MINI PROJECT
# ==========================================
# example.
import pandas as pd
student = {
"Name":["Sumit","Rahul","Amit"],
"Age":[20,21,19],
"Marks":[91,82,95]
}
df = pd.DataFrame(student)
print(df)
print()
print("Average Marks :",df["Marks"].mean())
print("Highest Marks :",df["Marks"].max())
print("Lowest Marks :",df["Marks"].min())

# Pandas = Python Library jo Table Data ko Read, Analyze aur Manage karne ke liye use hoti hai.
# to finally aaj hamar day 37 complete ho gaya
# is topic ko acche se practice karna.
# to chalo milte hai day 38 mai
# ek naya python concept ke saath tab tak ke liye,
# JAI HIND 🇮🇳
# JAI BHARAT 🇮🇳