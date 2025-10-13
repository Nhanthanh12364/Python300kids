my_set = {'Trung', 'tró', 12, 3, 6, 4, 'hihi'}
b = input()
try:
    b = int(b)
except:
    try:
        b = float(b)
    except:
        pass
if b in my_set:
    print(f'Phần tử {b} có tồn tại trong set')
else:
    print(f'Phần tử {b} không tồn tại trong set')
