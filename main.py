from pyunpack import Archive


# Archive(filename="MicroTik.rar", password="123").extractall(".")

pass_lab = ""

with open("pass.txt") as f:
    pass_lab = f.readlines()


print(pass_lab)
