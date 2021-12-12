a = (lambda x: x**2)(4)

print(a)

b = (lambda x,y: x**2 + y**2)(5,5)

print(b)

c = (lambda *args: sum (args) / len (args))(4,2)
print(c)

list=["Mufida"]
d= (lambda s:"-".join(set(s)))(list)

print(d)