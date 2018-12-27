import math
def prime(n):
    a=True
    if(n==1):
        print False
    if(n==2):
        print True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            a=False
    return a

def count(n):
    count=0
    i=n+1
    while(count<1):
        if(prime(i)):
            print i
            
n=input("enter the number")
print(prime(int(n)))