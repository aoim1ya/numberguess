import random

while True:
    a = random.randint(100,999)
    c = 0
    s = str(a)
    for j in range(9):
        if str(a).count(str(j)) > 1:
            c += 1
    if c == 0:
        break
            
            

g = list((str(a)))

def check():
    global n
    while True:
        a = str(int(input("Nhap so co 3 chu so khac nhau: ")))
        c = 0
        for j in range(0,10):
            if str(a).count(str(j)) > 1:
                c += 1
        if c == 0 and int(a) > 100 and int(a) < 1000:
            n = list(a)
            break
        if c != 0 or int(a) < 100 or int(a) > 999:
            print('Nhap sai yeu cau')
    
check()

while True:
    l = []
    dung = 0
    nuadung = 0
    for i in range(len(n)):
        if n[i] in g and n[i] not in l:
            if n[i] == g[i]:
                dung += 1
            elif n[i] not in l:
                nuadung += 1
            l.append(n[i])
            
                
    if dung < 3:
        if dung > 0:
            print(dung, " so dung va dung vi tri")
        if nuadung > 0:
            print(nuadung, " so dung va sai vi tri")
        if dung == 0 and nuadung == 0:
            print("Ban da doan sai")
            print("So do la", a)
        while True:
            n = list(str(int(input("Nhap so: "))))
            if int(''.join(n)) < 100 or int(''.join(n)) > 999:
                print("Nhap sai yeu cau")
            else:
                break
        
    if dung == 3:
        print("Ban da doan dung so", a)
        break
    
    
        
    