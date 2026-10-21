l = list(map(int, input().split()))
target = 24
for i in range(len(l)):
    for j in range(i, len(l)):
        sl = l[i:j+1]
        if len(sl) == 3 and sum(sl) == target:
            print(sl)