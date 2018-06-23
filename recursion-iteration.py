def do_this(stuff):
        s = ''
        while len(stuff) !=0:
                return str(stuff[0] * 2) + do_this(stuff[1:])
        return s
print(do_this([1,2,3]))

