# Python program to sort a list using a single loop
l1 = [34,12,90,56,2,123,1]
i = 0

try:
    while i < len(l1) - 1:
        if l1[i] > l1[i+1]:
            temp = l1[i]
            l1[i] = l1[i+1]
            l1[i+1] = temp
            i = -1    
        i += 1
except:
    print("Could not sort the list")

print(l1)