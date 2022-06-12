s = "Hackerrank.com presents \"Pythonist 2\""
s1 = []
s2 = []
for i in s:
    s1.append(i)
print(s1)
for i in s1:
    if i.isupper():
        s2.append(i.lower())
    else:
        s2.append(i.upper())
print(s2)
s = "".join(s2)
print(s)