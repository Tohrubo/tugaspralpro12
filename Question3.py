file1 = input("Insert Name for File 1: ")
file2 = input("Insert Name for File 2: ")

try:
    handle1 = open(file1, "r")
    handle2 = open(file2, "r")
except:
    print("Cannot find file")
    exit()

wf1s = set()
for lines1 in handle1:
    sen1 = lines1.split()
    for word1 in sen1:
        lw1 = word1.lower()
        wf1s.add(lw1)
wf2s = set()
for lines2 in handle2:
    sen2 = lines2.split()
    for word2 in sen2:
        lw2 = word2.lower()
        wf2s.add(lw2)

wordint = wf1s & wf2s
print(wordint)

handle1.close()
handle2.close()