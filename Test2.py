# TODO : GATHER ALL LISTS AND REMOVE DUPLICATES
# TODO : EXECUTE THE TEST ON THE OLD FILES WITH THE WEBSITE CONTENT
# TODO : PREPARE STATISTICS (CHECK EVERY WORD AND MARK ONLY NOMATCH KEYWORDS)

# import modules and defining values
import requests, bs4


list_of_keywords = ["",tutaj "będzie", "lis3%ta", "popojaa"]
fuzzy_search = []
w_slowniku = []
page_content = []

for element in list_of_keywords:
    url = "https://pl.pons.com/tłumaczenie?q=" + element + "&l=frpl&in=&lf=fr&qnac="
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print("There was a problem: %s" % (exc))
    for chunk in res.iter_content(100000):
        page_content.append(chunk)
        encoding = "utf-8"
        text_encoded = page_content[0].decode(encoding)
        print(text_encoded)
        if "fuzzysearch" in text_encoded:
            fuzzy_search.append(element)
        elif "no-dict-results" in text_encoded:
            fuzzy_search.append(element)
        else:
            w_slowniku.append(element)
print("fuzzy_search:", fuzzy_search)
print("w_slowniku:", w_slowniku)
