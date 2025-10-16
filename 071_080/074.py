file_path = 'example.txt' 
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        cnt = 0
        for line in f:
            a = list(line.split())
            cnt += len(a)
        print(f'Số lượng từ trong file là: {cnt}')
except FileNotFoundError:
    print(f'File {file_path} không tồn tại')
except Exception as e:
    print(f'Đã xảy ra lỗi: {e}')

#for line in f: print(sum(len(line.split() for line in f)))