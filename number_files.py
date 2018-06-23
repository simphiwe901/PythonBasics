# displays user input in the form of a numbers
# Writes to file
# Simphiwe Mchunu
# 28 August 2015

f = open('numbers.txt','w')
while True:
    n = input('Enter number:\n')
    if n =='':break
    z = f.write(n+'\n')
f.close()

f = open('numbers.txt')
p =0
for i in f:
    i+=p
    p+=1
    print(i)
print(p)
