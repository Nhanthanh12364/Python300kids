def check(n):
    if n > 0:
        return "Số bạn nhập là số dương"
    elif n < 0:
        return "Số bạn nhập là số âm"
    else:
        return "Số bạn nhập là số 0" 

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(check(n))
            break
        except:
            print( 'Vui lòng nhập lại!')

            