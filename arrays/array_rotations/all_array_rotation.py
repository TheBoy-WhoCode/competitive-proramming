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
# Time complexity O(n)
def method3(d, n, ar):
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

# Method 4 Reversal Algorithm
# Time Complexity O(n)
def method4(d, n, ar):
    if d == 0:
        return
    d = d % n
    reversalAlgo(ar, 0, d-1)
    reversalAlgo(ar, d, n-1)
    reversalAlgo(ar, 0, n-1)
    print(ar)

def reversalAlgo(ar, start, end):
    while (start < end):
        temp = ar[start]
        ar[start] = ar[end]
        ar[end] = temp
        start += 1
        end -= 1

if __name__ == "__main__":
    d = int(input("Please Enter d value\n"))
    n = int(input("Please Enter Size (N) and space seprated array values\n"))
    ar = list(map(int, input().rstrip().split()))
    
    method4(d, n, ar)

