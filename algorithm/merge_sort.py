from typing import List


def merge(left_list, right_list):
    list = []
    for i in range(len(left_list + right_list)):
        if len(left_list) != 0 and len(right_list) != 0:
            if left_list[0] <= right_list[0]:
                list.append(left_list[0])
                del left_list[0]
            else:
                list.append(right_list[0])
                del right_list[0]
        else:
            left_list = left_list + right_list
            list += left_list
            break

    # print(list, ' list !!!')
    return list
# 추가 메모리를 merge 단계에서 사용함 ( 새로운 list 를 생성해야해서)


def merge_sort(list):
    if len(list) == 1:
        return list
    left_list = merge_sort(list[: int(len(list) / 2)])
    # print(left_list, 'left')
    right_list = merge_sort(list[int(len(list) / 2):])
    # print(right_list, 'right')
    list = merge(left_list, right_list)

    return list


print(merge_sort([5, 3, 2, 4, 1, 3, 5, 6, 7, 2, 0, 7, 4, 2]))
