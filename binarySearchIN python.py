def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid


    return -1

arr = input("enter sorted array :")
arr1 = list(map(int, arr.split(" ")))
print(arr1)
x = int(input("Find no = "))
result = binary_search(arr1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")