  def fibonacci_ke_n(n, memo):
    if n <= 1:
        return n
    
    if memo[n] != 1:
        return memo[n]
    
    memo[n] = fibonacci_ke_n(n - 1, memo) + fibonacci_ke_n(n - 2, memo)
    
    return memo[n]

def fib(n):
    memo = [-1] * (n + 1)
    
    return fibonacci_ke_n(n, memo)

if __name__ == "__main__":
    n = 5
    result = fib(n)
    print(result)
