# import calc_module
# print(calc_module.add(2,3))
# print(calc_module.sub(2,3))
# print(calc_module.mul(2,3))
# print(calc_module.div(2,3))

# from calc_module import add
# print(add(2,3))
# print(calc_module.add(2,3)) # 안됨
# print(sub(2,3))
# print(mul(2,3))
# print(div(2,3))

import calc_module as cm
print(cm.add(2, 3))
print(cm.sub(2, 3))
print(cm.mul(2, 3))
print(cm.div(2, 3))
