# from pyunpack import Archive
from typing import List

# Archive(filename="MicroTik.rar", password="123").extractall(".")


def set_window(length: int) -> List:
    result = []
    i = 0
    while i < length:
        i += 1
        result.append((0, i))
    return result


book_lst = []

with open("pass.txt") as f:
    for el in f.readlines():
        stroka = el.strip().split("/n")
        if stroka != ['']:
            book_lst.extend(stroka)


for i, el in enumerate(book_lst[0]):
    pass


print(set_window(10))
