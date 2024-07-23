def verificacion(users,nombre,clave):
    i = 1
    j = 0
    w = 0

    while w < len(users):
        w += 1
        if users[i - 1][j + 1] == nombre:
            
            if users[i - 1][j + 2] == clave:
                print ("VERIFICADO - %s" %(users[i - 1][j + 3]))
                return (users[i - 1][j + 3])
        else:
            if w == len(users):
                
                return -1

        i += 1



