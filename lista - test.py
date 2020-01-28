list1 = [
    "baba",
    "",
    "c%",
    "baba",
    "babol",
    "lkjhgdfsrwf sgsgshdhdndldmdnd ldkdmdndncjderoksksmaer",
    "baba",
    "babol",
    "$#",
    "efrpl",
]
print(len(list1))
print(list1)


list2 = []
print(list1)
print(len(list1))
i = 1
for element in list1:
    print(i, element)
    i += 1
    if (
        element == ""
        or len(element) > 50
        or "#" in element
        or "$" in element
        or "&" in element
        or "%" in element
        or "frpl" in element
    ):
        list2.append(element)

print(list2)

for element2 in list2:
    list1.remove(element2)

print(list1)
element = "efrpl"
print(element.find("efrpl"))
