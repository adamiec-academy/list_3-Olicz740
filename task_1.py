def is_perfect(k):
    dividors = []
    for i in range(1, k):
        if k % i == 0:
            dividors.append(i)
    if sum(dividors) == k:
        return True
    else:
       return False

def get_perfect_numbers(n):

    k = 100
    result = []
    for i in range(k):
        if is_perfect(k) is True and len(result) < n:
            result.append(i)
        else:
            k += 1

    return result
print(get_perfect_numbers(2))
