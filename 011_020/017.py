def power(a,b):
    res = 1
    for i in range(abs(b)):
        res *= a
    if b < 0:
        res = 1/res
    return res
if __name__ == '__main__':
    while True:
        try:
            a = float(input('Nhập cơ số: '))
            b = int(input('Nhập số mũ: '))
            print(power(a,b))
            break
        except ValueError:
            print('Vui lòng nhập số hợp lệ!')
