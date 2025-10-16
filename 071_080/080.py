file_path = 'example.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open('example2.txt', 'w', encoding='utf-8') as f:
        f.write(content)
        print(f'Nội dung đã được thêm vào file example2.txt')
except FileNotFoundError:
    print(f'Không tồn tại file có tên {file_path}')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')