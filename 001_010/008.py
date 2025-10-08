def check_list(data):
    dem_chan = 0
    dem_le = 0
    for x in data:
        if x % 2 == 0:
            dem_chan += 1
        else:
            dem_le += 1
    return dem_chan, dem_le
if __name__ == '__main__':
    while True:
        try:
            a = list(map(int, input().split()))
            res = False
            for x in a:
                if x < 0:
                    res = True
                    print('Vui lòng nhập số tự nhiên!')
                    break
            if res:
                continue
            so_chan, so_le = check_list(a)
            print(so_chan, so_le)
            break
        except ValueError:
            print('Vui lòng nhập số nguyên hợp lệ')
    
   