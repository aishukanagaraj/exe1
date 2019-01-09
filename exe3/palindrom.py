def Ispalindrom(n):
    flag="Is palindrome"
    num=n
    revnum=0
    while(n>0):
        temp=n%10
        revnum=revnum*10+temp
        n=n//10  
    if not(revnum==num):
        flag="Is not a palindrome"
        
    return flag
n=input("Enter the number")
print(Ispalindrom(n))
