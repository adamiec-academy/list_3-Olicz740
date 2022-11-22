def is_perfect(k):
    dividors = []
    for i in range(1, k):
        if k % i == 0:
            dividors.append(i)
    return sum(dividors) == k

def get_perfect_numbers(n):
    k = 10000
    result = []
    for i in range(1, k):
        if is_perfect(i) is True and len(result) < n:
            result.append(i)
        else:
            k += 1

    return result
print(get_perfect_numbers(3))
