a = list(map(int, input().split()))
b = input()
try:
    phan_tu_can_xoa = int(b)
except ValueError:
    try:
        phan_tu_can_xoa = float(b)
    except ValueError:
        phan_tu_can_xoa = b
if phan_tu_can_xoa in a:
    a.remove(phan_tu_can_xoa)
    print('Danh sách sau khi xoá:', a)
else:
    print('Phần tử không tồn tại trong danh sách')