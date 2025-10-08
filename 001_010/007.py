def check(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n <= 0:
                print('Vui lòng nhập số nguyên dương!')
                continue
            if check(n):
                print(n, 'là năm nhuận')
            else:
                print(n, 'không phải là năm nhuận')
            break
        except ValueError:
            print('Vui lòng nhập số nguyên hợp lệ!')
