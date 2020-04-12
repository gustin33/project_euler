def sum_fibonacci(n): 
    fib_nums = [1, 2]
    result = 2
    while fib_nums[1] + fib_nums[0] <= n:
        fib_nums.append(fib_nums[0]+ fib_nums[1])
        del fib_nums[0]
        if fib_nums[1] % 2 == 0:
            result += fib_nums[1]
    return result


print(sum_fibonacci(4*10**6))
