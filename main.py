#f = open("a.csv", "r", encoding="utf-8")
f = open("a.csv", "r")

s = []
for i in f:
    a = i.replace("\n", "").replace(",", ".").split(";")
    s.append([a[0], a[1], float(a[2]), float(a[3]), float(a[4])])
f.close()
print(*s, sep="\n")
