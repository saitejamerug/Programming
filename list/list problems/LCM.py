def check_multiple(li, ma):
    for i in li:
        if ma % i != 0:
            return False
    return True
l = list(map(int, input().split()))
Max = max(l)
M = Max
while True:
    if check_multiple(l, M):
        print(M)
        break
    M += Max