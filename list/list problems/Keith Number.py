n = int(input())
t = n
l = []
while t>0:
    r = t % 10
    l.append(r)
    t = t // 10
Sum = 0
while Sum <= n:
    Sum = sum(l)
    if Sum == n:
        print("It's a Keith Number")
        break
    l.pop()
    l.insert(0, Sum)
if Sum > n:
    print("It's not a Keith Number")