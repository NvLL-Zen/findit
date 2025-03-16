arr = [7,11,10,5,12,4,18,15]

def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr)):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(len(arr) - n - 1):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    

print(f"before {arr}")
bubble_sort(arr)
print(f"after {arr}")

