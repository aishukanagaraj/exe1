def oddevencount(n):
    counteven=0
    countodd=0
    while(n>0):
        temp=n%10
        if(temp%2==0):
            counteven+=1
        else:
            countodd+=1
        n=n//10
    return counteven,countodd
n=input("Enter the number")
print(oddevencount(n))