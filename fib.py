def fib(n):
  return 1 and n<=2 or fib(n-1)+fib(n-2)

while True:
    x = input()
    print( fib(eval(x)))
