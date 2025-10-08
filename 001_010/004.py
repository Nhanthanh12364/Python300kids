def tinh_tien_taxi(n):
    if n <= 1:
        tien = 10000
    elif n <= 10:
        tien = 10000 + (n-1)*8500
    else: 
        tien = 10000 + 9 * 8500 + (n-10)*7500
    return tien
if __name__ == '__main__':
    while True:
        try:
            n = float(input('Nhập số km đã đi:'))
            if n <= 0:
                print('Vui lòng nhập 1 số dương')
                continue
            else:
                print(tinh_tien_taxi(n))
            break
        except ValueError:
            print('Vui lòng nhập số nguyên hợp lệ!')