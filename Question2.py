lst = [1, 1, 2, 3, 4, 4, 5]
print(f"List = {lst}")

ls = set(lst)
print(f"List --> Set = {ls}")

lsl = list(ls)
print(f"List --> Set --> List = {lsl}")

tup = (1, 2, 3, 3, 3, 4, 5)
print(f"Tuple = {tup}")

ts = set(tup)
print(f"Tuple --> Set = {ts}")

tst = tuple(ts)
print(f"Tuple --> Set --> Tuple = {tst}")