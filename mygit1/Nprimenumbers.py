import math 
def isprime(n):
    a=True
    if(n==1):
        return False
    if(n==2):
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            a=False
    return a

def primenum(n):
    if(n>=2):
        print 2
    for i in range(3,n+1,2):
        if(isprime(i)):
            print i
n=input("enter the number")
print(int(primenum(n)))