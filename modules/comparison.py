def comparison(a, b):
    if b == 0:
        return False
    elif a == 0:
        return False
    else:
        return comparison(a-1, b-1)

