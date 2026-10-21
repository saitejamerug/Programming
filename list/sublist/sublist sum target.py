l = list(map(int, input().split()))
target = 14
for i  in range(len(l)):
    for j in range(i, len(l)):
        sl = l[i:j+1]
        if sum(sl) == target:
            print(sl)