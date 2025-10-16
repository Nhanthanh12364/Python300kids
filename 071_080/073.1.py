file_path = 'example.txt'
try:
    line_count = 0 
    with open(file_path, 'r', encoding= 'utf-8') as f:
        for line in f:
            line_count += 1
    print(f"File '{file_path}' có {line_count} dòng.")
except FileNotFoundError:
    print(f'File {file_path} không tồn tại')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')