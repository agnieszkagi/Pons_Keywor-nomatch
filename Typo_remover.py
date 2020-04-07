#! python3

print(
    """
    --------------------------------------------------------------------------------
    -------------------------------TYPO-REMOVER-------------------------------------
    --------------------------------------------------------------------------------"""
)


keywords_to_be_checked = input("Please enter the list of keywords to be checked : ")
keywords_to_be_checked = keywords_to_be_checked.lower().replace("'", "")

list_of_keywords_to_be_checked = keywords_to_be_checked.split(", ")
# removing duplicates
list_of_keywords_to_be_checked = list(set(list_of_keywords_to_be_checked))
print("The following keywords will be checked: ", list_of_keywords_to_be_checked)
print("Number of keywords to be checked: ", len(list_of_keywords_to_be_checked))

print(
    """
    --------------------------------------------------------------------------------
    Every keyword will be displayed on the screen.
    Please decide if the keyword should be added to the dictionnary by entering:
    T    -   for TYPO
    D    -   for DICTIONARY KEYWORD
    --------------------------------------------------------------------------------
"""
)
dictionary_keywords = []

for keyword in list_of_keywords_to_be_checked:
    print("KEYWORD: ", keyword)
    print("Please define using 'T' or 'D'")
    decision = input().upper()
    if decision == "D":
        dictionary_keywords.append(keyword)

print(
    "==========================PROCESSING=FINISHED======================================"
)
print()

print(
    "The following words have been defined as potential new dictionary keywords : ",
    dictionary_keywords,
)

print("Number of keywords : ", len(dictionary_keywords))

# TODO percentage, status lsty,ile słow zostało do sprawdzenia
