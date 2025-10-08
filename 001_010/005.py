def check(score):
    if score >= 8.5:
        return 'Xuất sắc'
    elif score >= 7.0:
        return 'Giỏi'
    elif score >= 5.5:
        return 'Khá'
    elif score >= 4.0:
        return 'Trung Bình'
    else:
        return 'Yếu'
if __name__ == '__main__':
    while True:
        try:
            a = list(map(float, input().split()))
            res = False
            for x in a:
                if x > 10 or x < 0:
                       print('Vui lòng nhập số thực từ 0 đến 10 hợp lệ')
                       res = True
                       break
            if res:
                continue   
            score = sum(a)/len(a)
            print('%.2f' %score)
            print(check(score))
            break
        except ValueError:
            print('Vui lòng nhập số thực hợp lệ!')


