anime = input("Favourite name character")

def a(name):
    return name.replace("a"," ")

def e(name):
    return name.replace("e","0")

def i(name):
    return name.replace("i","1")

def o(name):
    return name.replace("o","2")
def u(name):
    return name.replace("u","3")

ola = a(anime)
ola = e(ola)
ola = i(ola)
ola = o(ola)
ola = u(ola)

print(ola)

# x = Change(anime)
# x.a()
# x.e()
# x.i()
# x.o()
# x.u()
# print(x)
