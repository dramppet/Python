def calc_fib(num, memo):
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    elif num == 1:
        return 1
    result = calc_fib(num - 1, memo) + calc_fib(num - 2, memo)
    memo[num] = result
    return result

n = int(input())

print(calc_fib(n, {}))