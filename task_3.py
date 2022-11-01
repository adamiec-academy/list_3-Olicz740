def fibonacci(n):
    if n < 0:
        print("error")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def fibonacci_sequence(n):
    result=[]
    while len(result) != n:
        for i in range(n):
            result.insert(0,fibonacci(n-i-1) )

    return result
print(fibonacci_sequence(6))
