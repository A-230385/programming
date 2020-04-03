# This function says if a year is bisiest
def bisiest(n):
    if n % 4 == 0 or n % 400 == 0:
        print('The year {0} is bisiest.'.format(n))
    else:
        print('The year {0} is not bisiest.'.format(n))

