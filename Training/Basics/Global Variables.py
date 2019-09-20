a = 10

def read():
    print(a)

read()

def mod1():
    global a
    a = 5

def mod2():
    a = 15
    print(a)
read()

mod1()

read()

mod2()

read()