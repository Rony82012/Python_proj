def readable(n):
    a = n % 7
    b = (n-a) / 7

    print( "{} weeks, {} days.".format(a,b))

readable(10)
