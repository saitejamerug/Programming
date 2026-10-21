# wappp largest sublist whose sum is palindrome
def is_palindrome(n):
    t = n
    rev = 0
    while t>0:
        r = t % 10
        rev = rev * 10 + r
        t = t // 10
    return rev == n

l = list(map(int, input().split()))
s_ls = 0    # sum largest sublist
for i in range(len(l)):
    for j in range(i, len(l)):
        sl=l[i:j+1]
        s_sl = sum(sl)  # sum of sublist
        if s_ls < s_sl and is_palindrome(s_sl):
            ls = sl     # largest sublist, sublist
            s_ls = s_sl
print(ls)