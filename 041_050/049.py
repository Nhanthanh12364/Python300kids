my_dict = {'name': 'Trung', 
           'age': 19, 
           'address': 'Đồng Ngư', 
           'school': 'UET', 
           'hobby': 'ngủ'}
#1
print('Số lượng cặp key-value (Phương pháp 1):', len(my_dict))
#2
print('Số lượng cặp key-value (Phương pháp 2):', len(my_dict.items()))
#3
cnt = 0
for _ in my_dict:
    cnt += 1
print('Số lượng cặp key-value (Phương pháp 3):', cnt)
