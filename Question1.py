n = int(input("Input Category amount: "))

categ = {}

for i in range(n):
    cname = input("Input Category name: ")

    apps = []
    for j in range(5):
        appname = input("App name: ")
        apps.append(appname)

    categ[cname] = apps

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