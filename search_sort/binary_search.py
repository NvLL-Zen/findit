arr = [1,2,3,4,5,6,7,8,9,10,11,12]

def search(target, start, end):

    if (start > end):
        return "not found"

    middle = round((start+end)/2)
    print(arr[start:end])

    if arr[middle] == target:
        return f"Found at index: {middle}"

    if arr[middle] > target:
        return search(target, start, middle-1)

    if arr[middle] < target:
        return search(target, middle+1, end)


print(search(4, 0, 12))