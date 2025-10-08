import math
C = lambda x: 2 * math.pi * x
S = lambda x: math.pi * x ** 2
while True:
    try:
        r = float(input('Nhập bán kính: '))
        if r < 0:
            print('Bán kính phải là số không âm')
            continue
        else:
            print('Chu vi hình tròn là:', '%.2f' %C(r))
            print('Diện tích hình tròn là:', '%.2f' %S(r))
            break
    except ValueError:
        print('Vui lòng nhập số hợp lệ!')