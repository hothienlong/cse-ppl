def lessThan_a(n, lst):
    return [element for element in lst if element < n]

def lessThan_b(n, lst):
    if lst == []:
        return lst
    x = lst[0]
    if x < n:
        return [x] + lessThan_b(n, lst[1:]) #phần tử đầu + chuỗi bị cắt
    else:
        return lessThan_b(n, lst[1:]) #chuỗi bị cắt

def lessThan_c(n, lst):
  return list(filter(lambda item: item<n, lst))



# lst = lessThan_b(50, [1,55,6,2])
# for i in lst:
#     print(i)