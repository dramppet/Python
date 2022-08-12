def calc_fib(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
    memo[n] = result

    return result

num_fib = int(input())

print(calc_fib(num_fib, {}))