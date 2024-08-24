number=int(input("enter a number"))
cnt=0
for i in range(2,int(number/2+1)):
    if number%i==0:
        cnt=cnt+1
if cnt==0:
    print(f"{number} is a prime number")
else:
    print("not a prime number")