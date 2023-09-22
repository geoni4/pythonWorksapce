# comprehension

a = [1, 2, 3 ,4]

result = [num *3 for num in a]

# print(result)

result2 = [num*3 for num in a if num % 2 == 0]

# print(result2)

result = [ x * y for x in range(1, 10) for y in range(1, 10)]

def colmulrow():
  for x in range(1, 10):
    for y in range(1, 10):
      return x  * y

# print(result)


def sum(a, b):
  return a+b

a, b = 3, 4

c = sum(a, b)

# print(c)

def sum_print(a = 4, b= 5):
  print(f'a는 {a} b는 {b} 입니다')
  
# sum_print(a, b)

def say():
  print('HI')
  
# say()

sum_print()

sum_print(b = 9, a = 3)
