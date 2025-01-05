unsorted_list=random.sample(range(1,100),10)
print(f"Unsorted list: {unsorted_list}")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
sorted_list = bubble_sort(unsorted_list)
print(f"Sorted list: {sorted_list}")
