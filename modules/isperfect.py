def isperfect(n):
    summ = 0
    for i in range(1, n):
        if n % i == 0:
            summ += i
    if summ == n:
        return True
    else:
        return False


