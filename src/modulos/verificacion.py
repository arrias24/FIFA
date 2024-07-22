
def verificacion(users,nombre,clave):
    i = 0
    j = 0
    w = 0
    print(len(users))
    while w < len(users):
        w += 1
        if users[i - 1][j + 1] == nombre:
            
            if users[i - 1][j + 2] == clave:
                print ("usuario verificado.. es un %s" %(users[i - 1][j +3]))
                return
        else:
            if w == len(users):
                print("Error usuario invalido...")

        i += 1
        j += 1
        



