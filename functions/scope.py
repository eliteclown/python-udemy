counter =100


def check():
    counter=90
    def innerCheck():
        nonlocal counter
        counter = 80
        print("Inner Counter:", counter)
    innerCheck()
    print("Outer Counter:", counter)
    

def check2():
    global counter
    counter = 70
    print("Global Counter inside check2:", counter) 

check()
check2()
print("Global Counter:", counter)