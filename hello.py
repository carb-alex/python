#hello world
print("Hello World")

#简单四则运算器
##需要注意类型转换，input获取的值是字符串，做计算需要转换成整数
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))

print("a+b =",a+b)
print("a-b =",a-b)
print("a*b =",a*b)
print("a/b =",a/b)

##元祖：不可变序列1
t=('hexuan','alex')
print(type(t))

##列表：可变序列
l=["hexuan"]
print(type(l))

##字典：
d={"name":"hexuan"}
print(type(d))

##迭代遍历
for x in l:
    print(x)

for y in t:
    print(y)

for z in d:
    print(z)

for m,n in d.items():
    print(m)
    print(n)

##函数，参数传入元祖*args，传入字典**kwargs
def test(x,*args,**kwargs):
    if True:
        print(x)
        print(args)
        print(kwargs)

test(1,*t,**d)

##正则表达式
###普通字符
###一元字符 . ^ $ * + ? {} [] \ | ()