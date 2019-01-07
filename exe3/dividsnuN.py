#check if all number of N divids N
def numdivN(n):
    flag= True
    num = n 
    while(n>0):
        temp=n%10
        if(num%temp==0):
            flag=True
        else:
            flag = False
        n=n/10
    return flag
    #print rev
n=input("Enter the number:")
print(numdivN(n))