LIMIT = 10_000
arr = [0]*(LIMIT + 1)
def sum_divisors(n):
    out = 0
    for j in range(1, n):
        if n % j == 0:
            out += j
    return out
out = 0
candidate = 2
while candidate < LIMIT:
    if not arr[candidate]:
        pair = sum_divisors(candidate)
        if pair != candidate and pair <= LIMIT and sum_divisors(pair) == candidate:
            print(f"{candidate}, {pair}")
            arr[candidate] = 1
            arr[pair] = 1
            out += candidate
            out += pair
    candidate += 1
print(f"sum: {out}")
