'''
    Rotate array of size n by d elements

    n = 7, d = 2
    arr = {1, 2, 3, 4, 5, 6, 7}

    rotated_array = {3, 4, 5, 6, 7, 1, 2}
'''

# Method 1 Slicing
def method1(d, n, ar):
    split_array = ar[d: ] + ar[:d]
    print(split_array)

# Method 2 using temp variable
# Time Complexity O(n*d)
def method2(d, n, ar):
    for i in range(d):
        temp = ar[0]
        for i in range(n-1):
            ar[i] = ar[i + 1]
        ar[n-1] = temp
    print(ar)

# Method3 using GCD of n and d
def method3(d, n, ar):
    d  = d % n
    greatest_common_div = gcd(d, n)
    print("Value of D: ", d)
    print("Value of GCD: ", greatest_common_div)
    for i in range(greatest_common_div):
        temp = ar[i]
        j = i
        print("Value of j: ", j)
        while True:
            k = j + d
            print("Value of k: ", k)
            if k >= n:
                k = k-n
            if k == i:
                break
            ar[j] = ar[k]
            print("Value of ar[j]: ", ar[j])
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
    
    method3(d, n, ar)

