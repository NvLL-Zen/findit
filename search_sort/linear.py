arr = [2,5,4,6,19,23,11,10]
target = 23

def linearSearch(array, target):
    for n in range(len(arr)):
        if arr[n] == target:
            return f"Found {target} at index: {n}"

 
print(linearSearch(arr, target))