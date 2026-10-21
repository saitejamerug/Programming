def palindrome(n):
    temp = n
    rev = 0
    while temp>0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp // 10
    return rev == n
l = list(map(int, input().split()))
for i in range(len(l)):
    for j in range(i, len(l)):
        sl=l[i:j+1]
        if palindrome(sum(sl)):
            print(sl)