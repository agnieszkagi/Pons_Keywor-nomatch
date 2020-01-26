#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests, datetime
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.common.keys import Keys

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
    nomatch_keywords.replace("frpl - fr - keyword-nomatch (last 1h)</h3>", "")
    .replace("frpl - fr - keyword-nomatch (last 24h)</h3>", "")
    .replace("frpl - pl - keyword-nomatch (last 1h)</h3>", "")
    .replace("frpl - pl - keyword-nomatch (last 24h)</h3>", "")
    .replace("frpl - unknown - keyword-nomatch (last 1h)</h3>", "")
    .replace("frpl - unknown - keyword-nomatch (last 24h)</h3>", "")
    .replace("<br />", "|")
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

# Removing empty elements from the final list_of_nomatch_keywords
for element in list_of_nomatch_keywords:
    if element == "" or len(element) > 50:
        list_of_nomatch_keywords.remove(element)
print("Number of keywords before checking: ", len(list_of_nomatch_keywords))

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
input_elem = browser.find_element_by_id("q")
input_elem.clear()
input_elem.send_keys("test")
input_elem.send_keys(Keys.RETURN)
time.sleep(2)

input_elem2 = browser.find_element_by_class_name("pons-search-input")
input_elem2.clear()
input_elem2.send_keys("drugitest")
input_elem2.send_keys(Keys.RETURN)
final_list = []

"""
for keyword in list_of_nomatch_keywords:
    input_elem2.send_keys(keyword)
    if "fuzzysearch" in browser.page_source:
        final_list.append(keyword)
    input_elem2 = browser.find_element_by_class_name("pons-search-input")
    input_elem.send_keys(Keys.RETURN)
    time.sleep(3)




input_elem.clear()

print("Number of keywords AFTER checking: ", len(final_list))

print(final_list)
"""
