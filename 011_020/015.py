def Sum_digit(n):
    n = abs(n)
    tong = 0 
    while n != 0:
        tong += n % 10
        n //= 10
    return tong
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(Sum_digit(n))
            break
        except ValueError:
            print('Vui lòng nhập số nguyên hợp lệ!')
            
    

