

def draw_line(size,character='*'):
    for i in range(size):
                print (i*character,end='')
    return character
print(draw_line(4,'&'))
