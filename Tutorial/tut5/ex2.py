def flatten_a(lst):
    return [j for i in lst for j in i]


def flatten_b(lst):
    if lst == []:
        return lst
    return lst[0] + flatten_b(lst[1:])

from functools import reduce
def flatten_c(lst):
  return reduce(lambda lst1,lst2:lst1+lst2 ,lst)


# lst = flatten_b([[1,2,3],['a','b','c'],[1.1,2.1,3.1]])
# for i in lst:
#     print(i)