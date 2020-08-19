
# recursive implimentation
def recurse_factorial(n):
    if n == 0:
        return 1
    return n * recurse_factorial(n - 1)

print(recurse_factorial(5))

# iterative implimentation
def inter_factorial(n):
    answer = 1
    for i in range(n, 0, -1):
        answer *= i
    return answer
print(inter_factorial(5))