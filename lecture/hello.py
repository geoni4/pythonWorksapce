
"hello"


words = "hello world"

words[0]
words[0:5]
words[:5]
words[-1]


add= [1, 3, 5, 7, 9]
add
type(add)
type(words)

strList = ['life', 'is', 'too', 'short']
strList[0]

strList = [1, 2.1, 'life', 'is', 'short']


a = [1, 2, 3]

a

a.append(4)
a
a.reverse()
a
a.index(3)

t1 = (1, 2, 'a', 'b')

t2 = (3, 4)

print(t1 + t2)
print(t1)

dict = {'name' : 'pey', 'phone': '0119993323', 'birth': '1118'}
type(dict)

a = {'a': [1, 2, 3]}
a[2] = 'b'
print(a['a'])
del a['a']
print(type(dict.keys()))
d_list = list(dict.keys())
print(type(d_list))
for key in dict.keys():
  print(type(key))
  print(f'key: {key}')