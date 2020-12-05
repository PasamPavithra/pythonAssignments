#sorting
lst = [
    [102,'CCC',21000, 'm'],
    [100,'AAA',18000, 'f'],
    [101,'BBB',50000, 'm']
]
lst.sort()
print(lst,end=' ')

#prefixing and increment
l=len(lst)

for i in range(l):
    if(lst[i][3] == 'm'):
        lst[i][1] = 'Mr.' + lst[i][1]
    elif(lst[i][3] == 'f'):
        lst[i][1] = 'Ms.' + lst[i][1]
    lst[i][2] = lst[i][2] + (lst[i][2] * 0.1)

print(lst)