def fac (x) :
    if x < 0 :
        return None
    elif x == 0 :
        return 1
    else :
        return x * fac (x-1)



x = int (input (' adad bedeh : '))
print (' javab : ' , fac(x))
