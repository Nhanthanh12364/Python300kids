def is_palindrome(s):
    s = ''.join(x.lower() for x in s if x.isalnum())
    return s == s[::-1]
if __name__ == '__main__':
    input_string = input('Nhập một chuỗi: ')
    if is_palindrome(input_string):
        print(input_string, 'là palindrome.')
    else:
        print(input_string, 'không phải là palindrome.')