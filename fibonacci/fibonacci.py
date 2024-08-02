def fib(n: int, memo: dict = {}):
    if n in memo:
        # print(f"read from memo: {n} with value {memo[n]}")
        return memo[n]
    if n == 1 or n == 2:
        return 1
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
    

def main():
    print(fib(7))
    print(fib(20))
    print(fib(50))
    print(fib(100))

if __name__ == "__main__":
    main()