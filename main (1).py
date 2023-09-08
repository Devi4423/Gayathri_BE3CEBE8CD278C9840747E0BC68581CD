def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

n=int(input("enter a integer number:"))
result = factorial(n)
print(f"the factorial of {n} is {result}")