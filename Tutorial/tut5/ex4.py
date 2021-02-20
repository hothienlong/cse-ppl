def compose_a(*functions):
    assert (len(functions) != 0)
    if len(functions) == 1:
        return lambda x: functions[0](x)
    return lambda x: functions[0](compose_a(*functions[1:])(x))

def double(x):
    return 2*x

def increase(x):
    return x + 1

def square(x):
    return x ** 2


f = compose_a(square, increase, double)
print(f(3))


from functools import reduce
#trả về hàm gộp của 2 hàm
def compose2_b(func1, func2):
  return lambda x: func1(func2(x))

#thực hiện chức năng gộp 2 hàm cho hết list funcs
def compose_b(*funcs):
  return reduce(lambda func1,func2: compose2_b(func1,func2), funcs)
