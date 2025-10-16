file_path = 'example.txt'
try:
    with open(file_path, 'w', encoding= 'utf-8') as f:
        i = 1
        for _ in range(5):
            f.write(f'{i}: Đứa đọc file này học bài đi\n')
            i += 1
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f'Nội dung của file {file_path} là:')
        print(content) 
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')

