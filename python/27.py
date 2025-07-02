def Dani_pow (x,y) :
    if y == 1 :
        return x
    else :
        return Dani_pow (x,y-1) * x


x = int (input (' adad bedeh : '))
y = int (input (' adad bedeh : '))

print (' javab :  ' , Dani_pow(x , y))

