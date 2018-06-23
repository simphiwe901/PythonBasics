def sum_list(n):
    while len(n) !=0:
        return n[0]+sum_list(n[1:len(n)+1])
    return 0

    
print(sum_list([1,4,7]))
    