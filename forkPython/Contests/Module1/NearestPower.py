def nearestPower(a,b):
    ##Your code here
    ##return the closest power
    
    x=math.floor(math.log(b,a))
    y=x+1
    p=a**x
    n=a**y
    if(abs(p-b)>abs(n-b)):
        return n
    else:
        return p