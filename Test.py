#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests, datetime, sys, time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.keys import Keys


url = "https://top.pons.me/?dict=frpl"
file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + "_FINAL_LIST.txt"

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

print("Number of keywords to be checked in dictionary: ", len(list_of_nomatch_keywords))
print("List of keywords: ", list_of_nomatch_keywords)

# SELENIUM PART

# disable cookies:
ops = options()
ops.set_preference("network.cookie.cookieBehavior", 2)
browser = webdriver.Firefox(options=ops)
# loading the pons website
try:
    browser.get("https://pl.pons.com/t%C5%82umaczenie?q=&l=frpl&in=&lf=fr&qnac=")
except Exception as exc:
    print("There was a problem: %s" % (exc))
# keywords input
input_elem = browser.find_element_by_name("q")
input_elem.clear()
input_elem.send_keys("test")
input_elem.send_keys(Keys.RETURN)

final_list = []

for keyword in list_of_nomatch_keywords:

    time.sleep(4)

    input_elem2 = browser.find_element_by_name("q")
    input_elem2.clear()

    input_elem2.send_keys(keyword)
    input_elem2.send_keys(Keys.RETURN)

    time.sleep(4)

    if "fuzzysearch" in browser.page_source:
        final_list.append(keyword)
    elif "no-dict-results" in browser.page_source:
        final_list.append(keyword)

browser.quit()

print("Number of keywords BEFORE checking: ", len(list_of_nomatch_keywords))
print("Number of keywords AFTER checking: ", len(final_list))

print(final_list)

try:
    ponsFile = open(file_name, "w+")
    ponsFile.write("THE LIST OF KEYWORDS THAN DON'T EXIST IN DICTIONARY" + "\n" + "\n")
    for word in final_list:
        ponsFile.write(word + "\n")
    ponsFile.close()
    print("Final list has been saved in the new file:", file_name)
except:
    print("Something went wrong...", sys.exc_info()[0])

print("DONE")
