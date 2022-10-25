def function1():
    function2(4)
    function2(5)
    function2(6)
    print("function1 done successfully")

def function2(x):
    if x % 5 == 0:
        raise Exception("function2 failed")
    return x + 2

function1()
# drake was here