from math import*
def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
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