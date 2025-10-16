import os
file_path = 'example.txt'
if os.path.isfile(file_path):
    print(f'File {file_path} có tồn tại trong thư mục')
else:
    print(f'File {file_path} không tồn tại trong thư mục')