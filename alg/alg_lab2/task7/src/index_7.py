def max_subarray(arr):
    max_current = arr[0]
    max_global = arr[0]
    start_index = 0
    end_index = 0
    temp_start_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
            temp_start_index = i
        else:
            max_current += arr[i]
        if max_current > max_global:
            max_global = max_current
            start_index = temp_start_index
            end_index = i
    return  arr[start_index:end_index + 1]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n = int(file.readline())
        arr = [int(i) for i in file.readline().split()]
    with open("output.txt", "w") as file:
        if 0 <= n <= 2 * 10 ** 4 and min(arr) >= -10 ** 9 and max(arr) < 10 ** 9:
            max_subarr = max_subarray(arr)
            file.write(" ".join(str(a) for a in max_subarr))
        else:
            print("Число в массиве по модулю превосходит 10^9 или количсетво элементов не соответствует ограничниям")
