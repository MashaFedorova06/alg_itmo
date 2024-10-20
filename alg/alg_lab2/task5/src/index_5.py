def majority_element(arr):
    def find_candidate(start, end):
        if start == end:
            return arr[start]
        mid = (start + end) // 2
        left_candidate = find_candidate(start, mid)
        right_candidate = find_candidate(mid + 1, end)
        if left_candidate == right_candidate:
            return left_candidate
        else:
            return left_candidate if count_occurrences(left_candidate) > count_occurrences(
                right_candidate) else right_candidate

    def count_occurrences(cand):
        count = sum([1 for x in arr if x == cand])
        return count

    candidate = find_candidate(0, len(arr) - 1)
    occurrences_count = count_occurrences(candidate)
    if occurrences_count > len(arr) // 2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        n = file.readline()
        array = [int(i) for i in file.readline().split()]

    result = majority_element(array)

    with open('output.txt', 'w') as file:
        file.write(str(result))
