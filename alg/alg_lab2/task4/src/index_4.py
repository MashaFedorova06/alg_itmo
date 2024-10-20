def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def insertionSort(n,arr):
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n1 = int(file.readline())
        arr = [int(i) for i in file.readline().split()]
        insertionSort(n1,arr)
        n2 = int(file.readline())
        search_elements = [int(i) for i in file.readline().split()]

    with open("output.txt", "w") as file:
        results = []
        for element in search_elements:
            result = binary_search(arr, element)
            results.append(str(result))
        file.write(" ".join(results))
