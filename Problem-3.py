num = int(input("Enter a number: "))
count = num if num%2!= 0 else num - 1
sol = [str(2*i+1) for i in range(count)]
print(", ".join(sol))
