def loopuno():
    for i in range(10):
        for j in range(10):
            print(j, end =' ')
        print()

loopuno()

print()

def loopdos():
    for i in range(10):
        for j in range(10):           
            print(i, end =' ')
        print()
                            
loopdos()
print()

def looptres():
    for i in range(11):
        for j in range(i):
            print(j, end =' ')
        print()

print()



looptres()
print()

def loopquatro():
    for i in range(10):
        for j in range(i):
            print(' ', end =' ')
        for m in range(0, 10 - i):
            print(m, end =' ')
        print()
    
loopquatro()
print()

def loopcinco():
    l = 10
    for j in range(0,10):
        for h in range(0,j):
            print(l, end = ' ')
            l += 1
        print()

loopcinco()