import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def main():
    unsorted_list = random.sample(range(1, 100), 10)
    print(f"Unsorted list: {unsorted_list}")
    sorted_list = insertion_sort(unsorted_list)
    print(f"Sorted list: {sorted_list}")
main()