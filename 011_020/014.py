if __name__ =='__main__':
    while True:
        try:
            a = list(map(float, input().split()))
            if not a:
                print('Danh sách rỗng, không có số lớn nhất')
                continue
            print(max(a))
            break
        except ValueError:
            print('Vui lòng nhập số hợp lệ!')