file_path = 'example.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        filtered_content = ''.join(a for a in content if a not in (' ', '\n', '\t'))
        print(f'Số lượng kí tự trong file {file_path} là: {len(filtered_content)}')
except FileNotFoundError:
    print(f'File {file_path} không tồn tại')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')
              