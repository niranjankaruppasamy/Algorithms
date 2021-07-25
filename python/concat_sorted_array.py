a = [1, 3, 5, 7, 9, 15]
b = [2, 4, 6, 8, 10, 11, 12, 13, 14, 1000]
c = []
i = 0; j=0
arr_empty = False
while True:
    if a[i] <= b[j]:
        c.append(a[i])
        i+=1
        if i > len(a)-1:
            arr_empty = True
            for ind in range(j, len(b)):
                c.append(b[ind])
    else:
        c.append(b[j])
        j+=1
        if j > len(b)-1:
            arr_empty = True
            for ind in range(i, len(a)):
                c.append(a[ind])
    if arr_empty:
        break


print(c)