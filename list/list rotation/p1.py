# reverse only even nums in given list 
l = [1, 235, 3, 49, 58, 16, 7, 78, 9, 107]
def rev(n):
    rev = 0
    while n>0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev

for i in range(0, len(l)):
    if l[i] % 2 == 0:
        l[i] = rev(l[i])
print(l)