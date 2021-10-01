num_list = [1, 3, 6, 9, 12, 15, 18, 21, 22]


def binary_search(data, find_list, start, end):
    mid_num = start + (end - start) // 2  # 버림
    if find_list[mid_num] == data:
        return mid_num
    elif end - start == 1:
        return False
    elif find_list[mid_num] < data:
        return binary_search(data, find_list, mid_num, end)
    elif find_list[mid_num] > data:
        return binary_search(data, find_list, start, mid_num)


print(binary_search(int(input()), num_list, 0, len(num_list)))
