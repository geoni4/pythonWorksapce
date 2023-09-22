s1 = set([1, 2, 3])

s1.add(4)
s1.update([5, 6, 7])
s1


a = True
type(a)

b = 1 + 1j
c = 2 - 3j

d = b + c

d

a = 1

id(a)


money = 1
if money:
    print("택시 타고 가라")
else:
    print("걸어가라")


if money:
    print("택시 타고 가라")
else:
    print("걸어가라")


pocket = ["paper", "cellphone", "money"]


if "money" in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if "money" in pocket:
    pass
else:
    print("걸어가라")


card = 1
if "money" in pocket:
    print("택시 타고 가라")
elif card:
    print(" 택시 타고 가라")
else:
    print("걸어가라")


num = 1
while num <= 10:
    print("Hello world", num)
    num = num + 1
