a = (2, 4826, 7464, 172, 1019, -193, -347,0)
min_value = a[0]
for x in a:
    if x < min_value:
        min_value = x
print('Phần tử nhỏ nhất trong tuple là', min_value)