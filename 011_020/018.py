def c_f(c):
    return c * 9 / 5 + 32
if __name__ == '__main__':
    while True:
        try:
            c = float(input())
            f = c_f(c)
            print(f)
            break
        except ValueError:
            print('Vui lòng nhập số hợp lệ!')