#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests, datetime, sys

url = "https://top.pons.me/?dict=frpl"
file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + "_NOMATCH_KEYWORDS.txt"

# Download the page and saving the content in the top_list variable

print("Downloading page %s..." % url)

res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))

top_list = []

for chunk in res.iter_content(100000):
    top_list.append(chunk)

# decoding text and spliting it using '<h3>'
encoding = "utf-8"
text_encoded = top_list[0].decode(encoding)
keyword_list = text_encoded.split("<h3>")
nomatch_list = []


for element in keyword_list:
    if element.find("keyword-nomatch") != -1:
        nomatch_list.append(element)

nomatch_keywords = "".join(nomatch_list)

# Replacing phrases and special characters that are not dictionary keywords
# Storing text with nomatch keywords in no_special_characters

no_special_characters = (
    nomatch_keywords.replace("<br />", "|")
    .replace(":", "|")
    .replace("...", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" more", "")
    .replace(" ", "")
    .replace("\n", "")
)
print(no_special_characters)

# Removing digits from the text and storing the rest in no_digit
no_digit = "".join([i for i in no_special_characters if not i.isdigit()])

# changing no_digit text into list by spliting the keywords using |
list_of_nomatch_keywords = no_digit.replace("||", "|").split("|")

# Removing empty elements, special characters from the list_of_nomatch_keywords

unwanted_keywords = []
for element in list_of_nomatch_keywords:
    if (
        element == ""
        or len(element) > 50
        or "#" in element
        or "$" in element
        or "&" in element
        or "%" in element
        or "frpl" in element
    ):
        unwanted_keywords.append(element)

for unwanted_keyword in unwanted_keywords:
    list_of_nomatch_keywords.remove(unwanted_keyword)

print("Number of keywords to be checked in dictionary: ", len(list_of_nomatch_keywords))
print("List of keywords: ")
print(list_of_nomatch_keywords)

# Saving list of nomatch keywords into the .txt file

"""
try:
    ponsFile = open(file_name, "w+")
    for word in list_of_nomatch_keywords:
        ponsFile.write(word + "\n")
    ponsFile.close()
    print("List of nomatch keywords has been saved in the new file:", file_name)
except:
    print("Something went wrong...", sys.exc_info()[0])

# TODO : SELENIUM PART
# później wszystkie importy przenieść na górę
"""
# TODO: SPRAWDZIĆ CZY NA POCZĄTKU KODU POTRZEBNA JEST TAKA ILOŚĆ ZMIENNYCH
