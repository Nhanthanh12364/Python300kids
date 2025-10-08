def check(n):
    if n % 2 == 0:
        print('Số bạn nhập là số chẵn')
    else:
        print('Số bạn nhập là số lẻ')
if __name__ =='__main__':
    while True:
        try: 
            n = int(input())
            check(n)
            break
        except:
            print('Vui lòng nhập số nguyên hợp lệ!')