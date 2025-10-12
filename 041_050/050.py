dict1 = {
    'name': 'Alice',
    'age': 25
}
dict2 = {
    'city': ''
    'New York',
    'country': 'USA'
}
#1
dict3 = dict1.copy()
dict3.update(dict2)
print("Kết quả nối dictionary bằng phương thức update():", dict3)
#2
dict4 = {**dict1, **dict2}
print("Kết quả nối dictionary bằng toán tử **:", dict4)