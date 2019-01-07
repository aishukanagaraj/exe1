#amstrong number
def amstrongnum(n):
    temp=0
    sum=0
    num=n
    while(n>0):
        temp=n%10
        n=n//10
        sum+=temp**3
    if(sum==num):
        print "It is an amstrong number"
    else:
        print "Not an amstrong number"
n=input("enter the number")
amstrongnum(n)