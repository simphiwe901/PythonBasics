def power(num,exp):
    if exp ==0:
        return 1
    else:
        x = num**exp
        return x
def main():
    num = int(input('Enter num: '))
    exp =int(input('Enter exp: '))
    print(power(num,exp))
    
main()