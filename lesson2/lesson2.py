a = 5
b = a
c = a
print(a, b, c)
print(id(a))
print(id(b))
print(id(c))


k = 2,95
m = 0,6
print(id(k))
print(id(m))

a = bool (5)
b = float (5)
c = str(5)
print(a, b, c)
print(id(a))
print(id(b))
print(id(c))


k=m=list(k)
print(k,m)
print(id(k),id(m))

a = input("Введите строку")
s = a[1::2]
h = a[::2]
print("Введена строка", s, end="     ")
print("Введена строка", h,"!!!")














