l = list(map(int, input().split()))
for i in range(len(l)):
    for j in range(i, len(l)):
        sl=l[i:j+1]
        print(sl)