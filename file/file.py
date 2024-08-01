print("f.read(size)")
f = open("test.txt", "r")
str = f.read()
print(str)
f.close()

print("f.readline()")
f1 = open("test.txt", "r")
str1 = f1.readline()
print(str1)
f1.close()

print("f.readlines()")
f2 = open("test.txt", "r")
a = f2.readlines()
print(a)
f.close()

print("遍历文件")
f3 = open("test.txt", "r")
for line in f3:
    print(line, end='')
f3.close()

print("f.write()")
f4 = open("test.txt", "w")
f4.write("Python 是一种非常好的语言。\n我喜欢Python!!\n")
f4.close()

print("f.seek()")
fo = open("runoob.txt", "rb+")
print("文件名为: ", fo.name)

line = fo.readline()
print("读取的数据为: %s" % (line))

# 重新设置文件读取指针到开头
fo.seek(-2, 2)
line = fo.readline()
print("读取的数据为: %s" % (line))

# 关闭文件
fo.close()
