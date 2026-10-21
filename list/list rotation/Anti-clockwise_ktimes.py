# anti-clockwise with k times rotations 
l = [10, 20, 30, 40, 50]
k = int(input("Enter no.of rotations:"))
n = 0
for i in range(len(l), 0, -1):
    n += 1
    val = l[len(l)-1]
    for j in range(len(l)-1, 0, -1):
        l[j] = l[j-1]
    l[0] = val
    print(l)
    if k == n:
        break