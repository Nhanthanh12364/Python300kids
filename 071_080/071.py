try:
    with open('example.txt', 'r', encoding = 'utf-8') as f:
        content = f.read()
        print('Nội dung của file:')
        print(content)
except FileNotFoundError:
    print(f'Không tìm thấy file example.txt')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')




