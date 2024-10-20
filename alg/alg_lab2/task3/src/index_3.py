def merge_and_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count


def count_inversions(n, arr):
    temp_array = [0] * n
    return merge_sort_and_count(arr, temp_array, 0, n - 1)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n = int(file.readline())
        arr = [int(i) for i in file.readline().split()]

    with open("output.txt", "w") as file:
        if 0 <= n <= 2 * 10 ** 4 and min(arr) >= -10 ** 9 and max(arr) < 10 ** 9:
            inversions = count_inversions(n, arr)
            file.write(str(inversions))
        else:
            print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")
