# from pyunpack import Archive


# Archive(filename="MicroTik.rar", password="123").extractall(".")

book_lst = []

with open("pass.txt") as f:
    for el in f.readlines():
        stroka = el.strip().split("/n")
        if stroka != ['']:
            book_lst.extend(stroka)
            

book_ln = ''.join(book_lst)
