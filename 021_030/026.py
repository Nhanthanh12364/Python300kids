import random
a = list(map(int, input().split()))
random.shuffle(a)
print('Danh sách sau khi xáo trộn', a)
a.sort(reverse = True)
print('Danh sách sau khi sắp xếp', a)