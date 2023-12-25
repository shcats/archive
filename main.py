from pyunpack import Archive


# Archive(filename="MicroTik.rar", password="123").extractall(".")

book = []

with open("pass.txt") as f:
    for el in f.readlines():
        stroka = el.strip().split("/n")
        if stroka != ['']:
            book.append(stroka)


print(book[0])
