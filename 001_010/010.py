def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return abs(a)
if __name__ == '__main__':
    while True:
        try:
            a, b = map(int, input().split())
            print(gcd(a,b))
            break
        except ValueError:
            print('Vui lòng nhập số nguyên hợp lệ!')