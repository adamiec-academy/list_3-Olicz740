def get_perfect_numbers(n):
    k = 10
    divisors = [1]
    result = []
    for i in range(2, k):
        if (k % i) == 0:
            divisors.append(i)
    for i in range(k):
        if i == sum(divisors) and len(result) < n:
            result.append(i)
    return result
print(get_perfect_numbers(2))
