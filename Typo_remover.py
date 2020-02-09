#! python3

keywords_to_be_checked = ""
keywords_to_be_checked = input("Please enter the list of keywords to be checked : ")
keywords_to_be_checked = keywords_to_be_checked.replace("'", "")
# TODO : REMOVE DUPLICATE FROM THE LIST

list_of_keywords_to_be_checked = keywords_to_be_checked.split(", ")
print("The following keywords will be checked: ", list_of_keywords_to_be_checked)

print(
    """
    Every keyword will be displayed on the screen.
    Please decide if the keyword should be added to the dictionnary by entering:
    T    -   for TYPO
    D    -   for DICTIONARY KEYWORD
"""
)
dictionary_keywords = []

for keyword in list_of_keywords_to_be_checked:
    print(keyword)
    print("Please define using 'T' or 'D'")
    decision = input()
    if decision == "D":
        dictionary_keywords.append(keyword)

print(
    "The following words have been defined as potential new dictionary keywords : ",
    dictionary_keywords,
)
