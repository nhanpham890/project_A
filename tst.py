
from cmath import sqrt
import math

def option():
     print('1: ax^2 + bx + c \n2: anX + bnY = Cn\n3: ax^4 + bx^2 + c = 0')


def ptr_bac_hai(a, b, c):
    while True:
        if a == 0 :
            print('so a phai la so khac 0 xin moi nhap lai so khac')
            a = float(input('xin moi nhap so a: '))
        else:
            break
    delta = b**2 - 4*a*c
    if delta < 0:
        print('ptr vo nghiem')
    elif delta == 0:
        print('ptr tren co nghiem kep x1= x2' , -(b/(2*a)))
    else:
        print('ptr co 2 nghiem phan biet ')
        print("x1 = ", (-(b) + math.sqrt(delta)) / (2 * a))
        print("x1 = ", (-(b) - math.sqrt(delta)) / (2 * a))
        return print('thanks for using our service')


def ptr_hai_an(a, b, c, d, e, f):
    D = a*e - d*b
    Dx = c*e - f*b                 #cthuc cramer
    Dy = a*f - d*c
    X = abs(Dx) / abs(D)
    Y = abs(Dy) / abs(D)
    print('the x la: ',X )
    print('the y la: ',Y )
    return print('thanks for using our service')


def ptr_trung_phuong(a,b,c):
    if a == 0:
        if (b == 0) and (c == 0):
            print('ptr co vo so nghiem')
        elif (b == 0) and (c != 0):
            print('ptr vo nghiem !')
        else:
            if (-c/b) < 0:
                print('ptr vo nghiem')
            elif (-c/b) == 0:
                print('ptr co nghiem x = 0')
            else:
                t= -c/b
                print('co 2 nghiem: x1 = ',math.sqrt(t),'va x2=',-math.sqrt(t))
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('ptr vo nghiem')
        elif delta == 0:
            t = -b/(2*a)
            if t < 0 :
                print('ptr vo nghiem')
            elif t == 0:
                print('ptr co nghinem = 0')
            else:
                print('ptr co 2 nghiem: x1= ',math.sqrt(t),'va x2= ',-math.sqrt(t))
        else:
            t = 0
            t1 = ((-b + math.sqrt(delta)) / (2*a))
            t2 = ((-b - math.sqrt(delta)) / (2*a))
            if (t1 < 0) and (t2 < 0):
                print('ptr vo nghiem')
            elif t1 < 0:
                t = t2
                print('ptr co 2 nghiem phan biet x1= ',math.sqrt(t),'va x2=',-math,sqrt(t))
            else:
                print('ptr co 4 nghiem phan biet: x1= ',math.sqrt(t1),'x2= ',-math.sqrt(t1),'x3= ',math.sqrt(t2),'x4= ',-math.sqrt(t2))
    return print('thanks for using our service')


option()
chuc_nang = input()
if chuc_nang == '1':
    a, b, c = map(float, input ('a b c\n').split())
    print(ptr_bac_hai(a, b, c))
elif chuc_nang == '2':
    a, b, c, d, e, f = map(float,input('a1 b1 c1 a2 b2 c2\n').split())
    ptr_hai_an(a, b, c, d, e, f)
elif chuc_nang == '3':
    a, b, c = map(float, input ('a b c\n').split())
    ptr_trung_phuong(a,b,c)
else:
    option()


        









    
   


