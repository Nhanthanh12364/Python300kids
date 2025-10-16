import os
file_path = 'example1.txt'
try:
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f'File {file_path} đã được xoá ')
    else:
        print(f"File '{file_path}' không tồn tại.")
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')