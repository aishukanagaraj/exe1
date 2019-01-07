def countnum(n):
    count=0
    while(n>0):
        #temp=n%10
        n=n//10
        count+=1
    return count
n=input("enter the number")
print(countnum(n))