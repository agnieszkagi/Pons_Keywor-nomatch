#! python3
# program downloads content from top.pons.me/?dict=frpl

# import modules and defining values
import requests, datetime

url = "https://top.pons.me/?dict=frpl"
file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + "NOMATCH_KEYWORDS.txt"

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

# decoding text
encoding = "utf-8"
text_encoded = top_list[0].decode(encoding)
keyword_list = text_encoded.split("<h3>")
nomatch_list = keyword_list[7:13]
nomatch_keywords = "".join(nomatch_list)

# Replacing words that are not dictionary keywords

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

# print(no_special_characters)
no_digit = "".join([i for i in no_special_characters if not i.isdigit()])
list_of_nomatch_keywords = no_digit.replace("||", "|").split("|")

for element in list_of_nomatch_keywords:
    if element == "":
        list_of_nomatch_keywords.remove(element)
print(list_of_nomatch_keywords)

# TODO : SAVING LIST IN THE .TXT FILE
