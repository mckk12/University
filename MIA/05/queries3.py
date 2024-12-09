def less_or_equal_x(arr,  x):
    low = 0
    high = len(arr) - 1
    while high - low > 1:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid
        else:
            low = mid
    
    if arr[high] <= x:
        return high + 1
    elif arr[low] <= x:
        return low + 1
    else:
        return 0

    

sizes = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

for i in b:
    answer = less_or_equal_x(a,i)
    
    print(answer, end=" ")

