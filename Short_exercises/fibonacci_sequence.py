t=int(input("Place a number of terms: "))
print()

n1=0
n2=1
counter=0

if t<=0:
    print("Invalid value.")
elif t==1:
    print("1")
else:
    print("Fibonacci sequence up to ", t, ": ")
    while counter<t:
        print(n1, end=" ,")
        x=n1+n2
        n1=n2
        n2=x
        counter+=1

print("\n Have a nice day!")
input()