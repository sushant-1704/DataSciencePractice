def divby7(n):
    if n==0 and n==7:
        return True
    
    while n>=10:
        lastDig=n%10
        n//=10
        n=abs(n-2*lastDig)

    return n==0 or n==7

inp=int(input("Enter a number: "))

if divby7(abs(inp)):
    print("True")
else:
    print("False")