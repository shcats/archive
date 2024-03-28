from pyunpack import Archive
from typing import List
from pyunpack import PatoolError
import patoolib

from patoolib.util import log_info
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
for k in range(len(book_lst)):
    s = book_lst[k]
    len_s = len(book_lst[k])
    for w in set_window(len(book_lst[k])):
        i, j = w
        for _ in range(len_s):
            if j<=len_s:
                passwords.append([s[i:j]])
                i=i+1
                j=j+1
            else:
                continue


for el in passwords:
        try:
            patoolib.extract_archive(archive="MicroTik.rar", password=el[:], interactive=False)
        except Exception as e:
            print(e)

