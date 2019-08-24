def move(level, x, y, z):
    if level == 1:
        print(x, " ==> ", z)
    else:
        # 将level - 1层从x移动到y
        move(level - 1, x, z, y)
        print(x, " ==> ", z)
        # 将level - 1层从y移动到z
        move(level - 1, y, x, z)


print("输入汉诺塔层数：")
n = int(input())
if n <= 0:
    print("数字非法!")
else:
    move(n, "x", "y", "z")
