def f(x,n):
    for i in range(len(x)):
        if x[i]==n:
            return i
    return -1
print(f(['a','b','c','d'],'b'))
        