a = list(map(int, input().split()))
b = input()
try:
    phan_tu_can_dem = int(b)
except:
    try:
        phan_tu_can_dem = float(b)
    except:
        phan_tu_can_dem = b
cnt = a.count(phan_tu_can_dem)
print('Số lần xuất hiện của phần tử', phan_tu_can_dem, 'là:', cnt)
