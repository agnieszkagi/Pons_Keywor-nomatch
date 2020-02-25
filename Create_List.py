#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests

url = "https://top.pons.me/?dict=frpl"

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

# Decoding text and spliting it using '<h3>'
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

# Removing digits from the text and storing the rest in no_digit
no_digit = "".join([i for i in no_special_characters if not i.isdigit()])

# changing no_digit text into list by spliting the keywords using |
list_of_nomatch_keywords = no_digit.replace("||", "|").split("|")

# removing duplicates
list_of_nomatch_keywords = list(set(list_of_nomatch_keywords))

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

print("-----------------------------------------------------")
print("Number of keywords to be checked in dictionary: ", len(list_of_nomatch_keywords))
print("List of keywords to be added to the file : ", list_of_nomatch_keywords)

# Saving downloaded list into the file (appending existing file)

list_content = ""
for word in list_of_nomatch_keywords:
    list_content += "'" + word + "', "

file_name = r"/home/agnieszka/PycharmProjects/ATBSWP_SELENIUM/files_with_all_nomatches/9-29.02.2020_LIST.txt"
with open(file_name, "a") as myfile:
    myfile.write(list_content)
print("-----------------------------------------------------")
print("Keyword list has been saved in localisation: ", file_name)
