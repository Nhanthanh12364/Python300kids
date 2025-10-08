def gt(n):
    if n < 0:
        return "Giai thừa không nhận số âm"
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(gt(n))
            break
        except ValueError:
            print('Vui lòng nhập số hợp lệ!')