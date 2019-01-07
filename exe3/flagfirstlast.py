def lastfirst(n):
    flag=True
    if not (firstdigit(n)==lastdigit(n)):
        flag=False
    return flag
n=input("Enter the number")
lastfirst(n)
