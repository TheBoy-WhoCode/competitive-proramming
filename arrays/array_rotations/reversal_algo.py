'''
    Rotate array of size n by d elements

    n = 7, d = 2
    arr = {1, 2, 3, 4, 5, 6, 7}

    rotated_array = {3, 4, 5, 6, 7, 1, 2}
'''

# Time Complexity O(n)
def start_point(d, n, ar):
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
    
    start_point(d, n, ar)