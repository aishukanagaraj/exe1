def Ispalindromleneven(n):
    flag="Palindrome length is even"
    count=0
    num=n
    revnum=0
    while(n>0):
        temp=n%10
        revnum=revnum*10+temp
        count+=1
        n=n//10  
    if(num==revnum):
        print "palindrom"
    else:
        print "not palindrom"
    if not(count%2==0):
        flag="Palindrome length is odd"
    print "Number of digit count",count   
    return flag
n=input("Enter the number")
print(Ispalindromleneven(n))
