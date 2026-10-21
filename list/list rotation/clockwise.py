l = [20, 10, 20, 30, 60]
for i in range(0, len(l)):
    k = l[0]
    for j in range(0, len(l)-1):
        l[j] = l[j+1]
    l[-1] = k
    print(l)