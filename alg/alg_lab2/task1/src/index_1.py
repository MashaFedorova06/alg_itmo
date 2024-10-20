def merge(left_arr, right_arr):
    sorted_arr = []
    left_arr_index = right_arr_index = 0
    left_arr_length, right_arr_length = len(left_arr), len(right_arr)
    for _ in range(len(left_arr) + len(right_arr)):
        if left_arr_index < len(left_arr) and right_arr_index < len(right_arr):
            if left_arr[left_arr_index] <= right_arr[right_arr_index]:
                sorted_arr.append(left_arr[left_arr_index])
                left_arr_index += 1
            else:
                sorted_arr.append(right_arr[right_arr_index])
                right_arr_index += 1
        elif left_arr_index == left_arr_length:
            sorted_arr.append(right_arr[right_arr_index])
            right_arr_index += 1
        elif right_arr_index == right_arr_length:
            sorted_arr.append(left_arr[left_arr_index])
            left_arr_index += 1
    return sorted_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    left_arr = merge_sort(arr[:m])
    right_arr = merge_sort(arr[m:])
    return merge(left_arr, right_arr)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n = int(file.readline())
        arr = [int(i) for i in file.readline().split()]
    with open("output.txt", "w") as file:
        if 0 <= n <= 2 * 10 ** 4 and min(arr) >= -10 ** 9 and max(arr) < 10 ** 9:
            sorted_arr = merge_sort(arr)
            file.write(" ".join(str(a) for a in sorted_arr))
        else:
            print("Число в массиве по модулю превосходит 10^9 или количсетво элементов не соответствует ограничниям")
