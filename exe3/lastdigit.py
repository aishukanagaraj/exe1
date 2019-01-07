#to print the last digit of given number
def lastdigit(n):
    temp=0
    while(n>0):
        temp=n%10
        return temp
n=input("Enter the number")
print(lastdigit(n))