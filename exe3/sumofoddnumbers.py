def oddnumber(n):
    flag=False
    if(n%2!=0):
        flag=True
    return flag

def sumofodd(n):
    sum1=0
    count=0
    
    for i in range(1,n*2,2):
        if(oddnumber(i)):
            count+=1
            sum1+=i
            print i
    print "sum of first odd number",sum1
    #print "sum of digits",sum1
n=input("Enter the number")
print(sumofodd(n))