my_dict = {'name': 'Trung', 'age': 19, 'address': 'Đồng Ngư', 'school': 'UET', 'hobby': 'ngủ'}
Key_input = input()
try:
    Key_input = int(Key_input)
except:
    try:
        Key_input = float(Key_input)
    except:
        pass
if Key_input in my_dict:
    print(f'Giá trị của khoá {Key_input} là: {my_dict[Key_input]}')
else:
    print(f'Khoá {Key_input} không tồn tại')