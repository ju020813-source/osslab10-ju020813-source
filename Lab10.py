def divisors(n: int):
    if n <= 0:
        return []
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res
