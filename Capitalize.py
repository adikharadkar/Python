s = input()
s = s.split(" ")
l = []
for i in s:
    l.append(i.capitalize())
s = " ".join(l)
print(s)