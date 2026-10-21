def factor_check(li, mi):
    for i in li:
        if i % mi != 0:
            return False
    return True
l = list(map(int, input().split()))
Min = min(l)
while True:
    if factor_check(l, Min):
        print(Min)
        break
    Min -= 1