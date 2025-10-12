my_dict = {'name': 'Trung', 
           'age': 19, 
           'address': 'Đồng Ngư', 
           'school': 'UET', 
           'hobby': 'ngủ'}
key_input = input()
if key_input in my_dict:
    print(f'Khoá {key_input} có tồn tại trong dictionary.')
else:
    print(f'Khoá {key_input} không tồn tại trong dictionary.')