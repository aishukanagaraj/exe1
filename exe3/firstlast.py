def firstdigit(n):
    while(n>=10):
        n=n//10
    return (int(n))

def lastdigit(n):
    return (n%10)

def lastfirst(n):
    flag=True
    if not(firstdigit(n)==lastdigit(n)):
        flag=False
    return flag
    
        
n=input("Enter the number")
print(lastfirst(n))
