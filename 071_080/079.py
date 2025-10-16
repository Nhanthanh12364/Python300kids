file_path = 'example.txt'
content_to_append = '\nNhàn đã rất chăm chỉ và cố gắng hoàn thành file này!'
try:
    with open(file_path, 'a+', encoding='utf-8') as f:
        f.write(content_to_append)
        f.seek(0)
        print('Nội dung của file sau khi thêm là:')
        print(f.read())
except FileNotFoundError:
    print(f'Không tồn tại file có tên {file_path}')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')
