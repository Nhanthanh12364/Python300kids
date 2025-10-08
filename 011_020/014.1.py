def max_(data):
    max_value = data[0]
    for x in data:
        if x >= max_value:
            max_value = x
    return max_value

if __name__ =='__main__':
    while True:
        try:
            a = list(map(float, input().split()))
            if not a:
                print('Danh sách rỗng, không có số lớn nhất')
                continue
            print(max_(a))
            break
        except ValueError:
            print('Vui lòng nhập số hợp lệ!')