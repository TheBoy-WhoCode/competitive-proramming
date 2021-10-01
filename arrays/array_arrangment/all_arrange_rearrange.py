'''
    Rearrange an array such that arr[i] = i
    Given an array of elements of length N, ranging from 0 to N – 1. 
    All elements may not be present in the array. 
    If the element is not present then there will be -1 present in the array. 
    Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.
'''

def arrange_rearrange(ar):
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[j] == i:
                ar[j], ar[i] = ar[i], ar[j]

    for k in range(len(ar)):
        if ar[k] != k:
            ar[k] = -1

    print(ar)

if __name__ == "__main__":
    n = int(input("Please Enter Size (N) and space seprated array values\n"))
    ar = list(map(int, input().rstrip().split()))
    arrange_rearrange(ar)