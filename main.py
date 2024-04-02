from pyunpack import Archive
from typing import List


def set_window(length: int) -> List:
    result = []
    i = 0
    while i < length:
        i += 1
        result.append((0, i))
    return result


def start(passwd: List, pass_length: int | None = None):
    for p in passwd:
        try:
            Archive(filename="med_licgen.rar", password=p[:]).extractall(".")
        except Exception as e:
            print(e)


book_lst = []

with open("pass.txt") as f:
    for el in f.readlines():
        stroka = el.strip().split("/n")
        if stroka != ['']:
            book_lst.extend(stroka)

pass_dict = {}
passwords = []
for k in range(len(book_lst)):
    s = book_lst[k]
    len_s = len(book_lst[k])
    for w in set_window(len(book_lst[k])):
        i, j = w
        for _ in range(len_s):
            if j <= len_s:
                passwords.append([s[i:j]])
                i = i+1
                j = j+1
            else:
                continue

    pass_dict[k] = passwords.copy()
    passwords.clear()

# start(passwords=passwords)
