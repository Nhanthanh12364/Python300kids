from math import*
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
if __name__ =='__main__':
    while True:
        try:
            n = int(input())
            if check_prime(n):
                print(n, 'là số nguyên tố')
            else:
                print(n, 'không là số nguyên tố')
            break
        except ValueError:
            print('Vui lòng nhập số nguyên hợp lệ!')