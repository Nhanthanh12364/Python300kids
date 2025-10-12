my_dict = {'name': 'Trung', 
           'age': 19, 
           'address': 'Đồng Ngư', 
           'school': 'UET', 
           'hobby': 'ngủ'}
delete_key = input()
if delete_key in my_dict:
    my_dict.pop(delete_key)
    print(f'Đã xoá cặp key_value có khoá {delete_key}')
    print(f'Dictionary sau khi xoá: {my_dict}')
else:
    print(f'Khoá {delete_key} không tồn tại trong dictionary')