#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests, os, bs4, datetime

url = "https://top.pons.me/?dict=frpl"
file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + ".txt"

# Download the page and saving the content in txt file

print("Downloading page %s..." % url)
res = requests.get(url)
res.raise_for_status()

ponsFile = open(file_name, "wb")
for chunk in res.iter_content(100000):
    ponsFile.write(chunk)
ponsFile.close()

print("File ", file_name, " has been created.")
