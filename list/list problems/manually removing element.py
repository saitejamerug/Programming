l = list(map(int, input().split()))
n = int(input())
def counts(l):
    oc = 0
    for i in range(len(l)):
        if n == l[i]:
            oc += 1
    return oc

def removed_list(l):
    new_l = []
    for i in range(len(l)):
        if i == 0:
            if l[i] == n:
                new_l = l[i + 1:]
                return new_l
        elif i == len(l) - 1:
            if l[i] == n:
                new_l = l[:i]
                return new_l
        else:
            if l[i] == n:
                new_l = l[:i] + l[i + 1:]
                return new_l


repeated = counts(l)
if repeated:
    while repeated > 0:
        l = removed_list(l)
        repeated -= 1
    print(l)
else:
    print("No removing element")