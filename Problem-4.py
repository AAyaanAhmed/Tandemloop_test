nums = list(map(int, input("Enter numbers").split()))
res = {}

for i in range(1, 10):
    c = sum(1 for n in nums if n % i == 0)
    res[i] = c
print(res)
