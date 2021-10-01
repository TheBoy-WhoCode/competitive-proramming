'''
    Rotate array of size n by d elements

    n = 7, d = 2
    arr = {1, 2, 3, 4, 5, 6, 7}

    rotated_array = {3, 4, 5, 6, 7, 1, 2}
'''

# Rotation using Slicing
def slicing(d, n, ar):
    split_array = ar[d: ] + ar[:d]
    print(split_array)



if __name__ == "__main__":
    d = int(input("Please Enter d value\n"))
    n = int(input("Please Enter Size (N) and space seprated array values\n"))
    ar = list(map(int, input().rstrip().split()))
    
    slicing(d, n, ar)

