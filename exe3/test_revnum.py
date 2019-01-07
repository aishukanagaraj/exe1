#Reverse a given integer N
def RevInteger(n):
    revnum=0
    while(n>0):
        temp=n%10
        revnum=revnum*10+temp
        n=n/10
    print revnum
n=input("Enter the number:")
RevInteger(n)