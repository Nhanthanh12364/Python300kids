if __name__ == '__main__':
    while True:
        try:
            a,b,c = map(int, input().split())
            print(max(a,b,c))
            break
        except Exception as e:
            print(e, 'Vui lòng nhập số nguyên hợp lệ!', sep= '. ')