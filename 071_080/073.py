file_path = 'example.txt'
try:
    with open(file_path, 'r', encoding= 'utf-8') as f:
        line_count = sum(1 for line in f)
        print(f'Số lượng dòng của file {file_path} là: {line_count}')
except FileNotFoundError:
    print(f'File {file_path} không tồn tại')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')
'''
#Cách 1:
with open(file_path, 'r', encoding= 'utf-8') as f:
    line_count = len(f.readlines())
print(f'File {file_path} có số dòng là: {line_count}')
#Cách 2:
line_count = 0 
with open(file_path, 'r', encoding= 'utf-8') as f:
    for line in f:
        line_count += 1
    print(f"File '{file_path}' có {line_count} dòng.")
'''