# Rev given list (Best approach)
l = list(map(int, input().split()))
print(l)
s = 0
e = len(l) - 1
while s<e:
    if l[s] % 2 == 0 and l[e] % 2 == 0:
        l[s], l[e] = l[e], l[s]
    s += 1
    e -= 1
print(l)