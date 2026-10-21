n=int(input("Enter number"))
list_c=[int(x) for x in str(n)]

su=0
while su<n:
    su=su*0+sum(list_c)
    if su != n:
        list_c.append(su)
        list_c.pop(0)
if su==n:
    print("True")
else:
    print("flase")