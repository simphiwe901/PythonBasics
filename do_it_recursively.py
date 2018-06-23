# recursion to iteration 
# Simphiwe Mchunu
# 18 August 2015

def do_it_recursively(n):
    z = 1
    i = 1
    while n !=0:
        for x in range(n,-1,-2):
            x*=x-2
        return x
    return z
    
print(do_it_recursively(2))
        