def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left_half = merge_sort(string[:mid])
    right_half = merge_sort(string[mid:])

    return merge(left_half, right_half)


def merge(left_half, right_half):
    ordered_string = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            ordered_string.append(left_half[i])
            i += 1
        else:
            ordered_string.append(right_half[j])
            j += 1

    ordered_string.extend(left_half[i:])
    ordered_string.extend(right_half[j:])

    return "".join(ordered_string)


def is_anagram(first_string, second_string):
    first_sorted = merge_sort(first_string.lower())
    second_sorted = merge_sort(second_string.lower())

    if not first_sorted or not second_sorted:
        return first_sorted, second_sorted, False

    return first_sorted, second_sorted, first_sorted == second_sorted
