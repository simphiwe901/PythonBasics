def do_this(stuff):
    if len(stuff)==0:
        return ''
    return str(stuff[0]*2) + do_this(stuff[1:])
print(do_this('123'))
        