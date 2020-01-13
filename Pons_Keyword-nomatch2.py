#! python3
# program downloads content from top.pons.me/?dict=frpl

#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests, datetime

url = "https://top.pons.me/?dict=frpl"
file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + ".txt"

# Download the page and saving the content in txt file

print("Downloading page %s..." % url)
res = requests.get(url)
res.raise_for_status()

keyword_list = []

for chunk in res.iter_content(100000):
    keyword_list.append(chunk)

encoding = "utf-8"
texto = keyword_list[0].decode(encoding)
nomatch_list = texto.split("<h3>")


# print(texto)

# print(nomatch_list[7])

"""
ponsFile = open(file_name, "wb")
for chunk in res.iter_content(100000):
    ponsFile.write(chunk)
for line in file_name:
    file_content += line
ponsFile.close()

# nomatch_list = file_content.split("<h3>")

# print(nomatch_list[2])
print(file_content)
"""
