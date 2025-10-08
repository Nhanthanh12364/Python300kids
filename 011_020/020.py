def chuvi(a,b):
    return 2 * (a+b)
def dientich(a,b):
    return a*b
if __name__ =='__main__':
    while True:
        try:
            a = float(input('Nhập chiều rộng: '))
            b = float(input('Nhập chiều dài: '))
            if a <= 0  or b <= 0 :
                print('Cạnh hình chữ nhật phải là số không âm')
                continue
            else:
                print('Chu vi hình chữ nhật là', chuvi(a,b))
                print('Diện tích hình chữ nhật là', dientich(a,b))
                break
        except ValueError:
            print('Vui lòng nhập số hợp lệ!')
            
            
