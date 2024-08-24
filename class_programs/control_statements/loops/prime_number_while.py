n = int(input("Enter a number to find the given number is Prime or not: "))
i = 2

if n > 0:
    if n == 1:
        print(f"{n} is not a prime number")
    else:
        while i < n:
            if n % i == 0:
                print(f"{n} is not a Prime number")
                break
            i = i + 1
        else:
            print(f"{n} is  a Prime Number")
else:
    print("Prime number is applied to only positive numbers")
