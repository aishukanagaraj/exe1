#To print the first digit
def firstdigit(n):
    while(n>=10):
        n=n//10
    return n
n=input("enter the number:")
print(firstdigit(n))
