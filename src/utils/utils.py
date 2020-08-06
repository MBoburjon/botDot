def to_nx2_matrix(arr):
    return [arr[i:i + 2] for i in range(0, len(arr), 2)]


from enum import IntEnum
    # TODO:


class MenuLevel(IntEnum):
    MAIN = 0
    ITEMS = 1
    QUANTITY = 2
    BASKET = 3
    ORDER = 4
    SHARE_CONTACT = 5
    SHARE_LOCATION = 6
    BACK = -1
