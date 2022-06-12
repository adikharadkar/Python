n = int(input())
arr = map(int, input().split(" "))
arr = list(arr)
for i in range(0, n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr[-2])