n=1
p=0
import time

sign=1.
while n<10000:
    
    if n%2==0:
        n=n+1
    else:
        p=p+4.*(sign/n)
        n=n+1
        sign=sign*(-1.)
    

pi = str(p)
print('Pi = ' + ''+ pi)
time.sleep(60)
