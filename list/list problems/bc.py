l = list(map(int, input().split()))
for i in range(len(l)):
    bc = 0
    for j in range(0, i+1):
        if l[i] == l[j]:
            bc += 1
    print(l[i], "->", bc)