def double_a(lst):
    return [2 * element for element in lst]

def double_b(lst):
    if lst == []:
        return lst
    return [2*lst[0]] + double_b(lst[1:])
# 2 * phần tử đầu + lst cũ bỏ phần tử đầu
    
def double_c(lst):
  return list(map(lambda x:x*2, lst))
