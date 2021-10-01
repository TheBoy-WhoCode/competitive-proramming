'''
    Rotate array of size n by d elements

    n = 7, d = 2
    arr = {1, 2, 3, 4, 5, 6, 7}

    rotated_array = {3, 4, 5, 6, 7, 1, 2}
'''


# Method3 using GCD of n and d
# Time complexity O(n)
def using_gcd(d, n, ar):
    d  = d % n
    greatest_common_div = gcd(d, n)
    for i in range(greatest_common_div):
        temp = ar[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k-n
            if k == i:
                break
            ar[j] = ar[k]
            j = k
        ar[j] = temp

    print(ar)

def gcd(d, n):
    if n == 0:
        return d
    else:
        return gcd(n, d % n)


if __name__ == "__main__":
    d = int(input("Please Enter d value\n"))
    n = int(input("Please Enter Size (N) and space seprated array values\n"))
    ar = list(map(int, input().rstrip().split()))
    
    using_gcd(d, n, ar)

