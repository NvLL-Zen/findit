arr = [7,11,10,5,12,4,18,15]

def bubble_sort(arr):
    for n in range(len(arr)):
        swapped = False

        for i in range(len(arr) - n - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
    

print(f"before {arr}")
bubble_sort(arr)
print(f"after {arr}")

counter = 0
swapped = False


