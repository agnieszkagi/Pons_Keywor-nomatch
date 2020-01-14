#! python3
# program downloads content from top.pons.me/?dict=frpl

#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests, datetime

url = "https://top.pons.me/?dict=frpl"
file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + ".txt"

# Download the page and saving the content in the top_list variable

print("Downloading page %s..." % url)
res = requests.get(url)
res.raise_for_status()

top_list = []

for chunk in res.iter_content(100000):
    top_list.append(chunk)

encoding = "utf-8"
texto = top_list[0].decode(encoding)
keyword_list = texto.split("<h3>")
nomatch_list = keyword_list[7:13]

print(nomatch_list)

# print(nomatch_list[7:13])
