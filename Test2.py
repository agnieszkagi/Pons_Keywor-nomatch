# TODO : GATHER ALL LISTS AND REMOVE DUPLICATES
# TODO : EXECUTE THE TEST ON THE OLD FILES WITH THE WEBSITE CONTENT
# TODO : PREPARE STATISTICS (CHECK EVERY WORD AND MARK ONLY NOMATCH KEYWORDS)

# import modules and defining values
import sys

list1 = []
filepath = r"/home/agnieszka/PycharmProjects/ATBSWP_SELENIUM/FINAL_LISTS/2020-01-26_20:42_FINAL_LIST.txt"

try:
    with open(filepath, "r") as file:
        for line in file:
            word = line.replace("\n", "")
            list1.append(word)
            # line = line.replace("\n", ",")
except:
    print("Something went wrong...", sys.exc_info()[0])
print(list1)
