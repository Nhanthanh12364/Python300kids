file_path = 'example.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end = '')
except FileNotFoundError:
    print(f'Không tồn tại file có tên {file_path}')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')
