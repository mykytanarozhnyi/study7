def gcd_classic(m,n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
            return m
def gcd_optimised(a,b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b

if __name__ == "__main__":
    gcd_classic(100,1)
    print ("============")
    gcd_optimised(27,6)
