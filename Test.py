categ = {
    "RPG" : ["Genshin", "Blue Archive", "FGO", "HSR", "WuWa"],
    "Anime" : ["Genshin", "FGO", "DAL", "Trails", "Blue Archive"],
    "Story" : ["Trails", "Ys", "Rance", "DAL", "FGO"],
}

applst = []

for app in categ.values():
    applst.append(set(app))

inres = applst[0]
for i in range(1, len(applst)):
    inres = inres & applst[i]

print("Exist in all: ",inres)

dcount = {}
for key, value in categ.items():
    for item in value:
        dcount[item] = dcount.get(item, 0) + 1

symdiffres = set()
for key, value in dcount.items():
    if value == 1:
        symdiffres.add(key)

print("Exist in Only 1: ",symdiffres)

twoinres = set()
for key,value in dcount.items():
    if value == 2:
        twoinres.add(key)

print("Exist in only 2: ",twoinres)