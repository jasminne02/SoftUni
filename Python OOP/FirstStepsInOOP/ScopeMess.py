x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"
        print(x)

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()

# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!
