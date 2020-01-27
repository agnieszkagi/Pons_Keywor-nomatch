list1 = [
    "baba",
    "",
    "%",
    "baba",
    "babol",
    "lkjhgdfsrwf sgsgshdhdndldmdnd ldkdmdndncjderoksksmaer",
    "baba",
    "babol",
    "$#",
]
print(len(list1))
print(list1)

i = 1
for l in list1:
    print(i, l)
    if (
        l == ""
        or len(l) > 50
        or l.find("#") > 0
        or l.find("$") > 0
        or l.find("&") > 0
        or l.find("%") > 0
    ):
        list1 = list1.remove(l)
    i += 1


# list1 = list(set(list1))
print(list1)
