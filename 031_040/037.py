a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = input('Nhập phần tử cần kiểm tra:')
try:
    b = int(b)
except:
    try: 
        b = float(b)
    except:
        pass
if b in a:
    print('YES')
else:
    print('NO')

