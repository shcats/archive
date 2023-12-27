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


passwords = []

for w in set_window(len(book_lst[0])):
    for i, el in enumerate(book_lst[0]):
        if (i+w[1])<len(book_lst[0]):
            print(book_lst[0][w[0+i]:w[1+i]])
        # passwords.extend(book_lst[0][w[0]:w[1]])
        else:
            continue



