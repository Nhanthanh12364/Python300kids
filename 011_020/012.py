if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            if n < 1:
                print('Vui lòng nhập số nguyên lớn hơn 1')
                continue
            print(n*(n+1)//2)
            break
        except ValueError:
            print('Vui lòng nhập số nguyên hợp lệ')