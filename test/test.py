a = 1  # 全局变量


def func():
    b = 2  # 局部变量
    print(a)  # 可访问全局变量a,无法访问它内部的c

    def inner():
        c = 3  # 更局部的变量
        print(a)  # 可以访问全局变量a
        print(b)  # b对于inner函数来说，就是外部变量
        print(c)

    inner()


func()
