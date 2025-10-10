a = (1,12,13,2,1,3,5,3,4,2,6,2,'28tech')
b = input()
try:
    b = int(b)
except:
    try:
        b = float(b)
    except:
        pass
print(a.count(b))