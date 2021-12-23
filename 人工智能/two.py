def calculate():
    try:  # 检测输入是否为数字
        num = eval(input("输入一个1-100的整数："))
        if type(num) == int:  # 检测是否为浮点数
            if 0 < num < 100:
                count = 0
                num_list = []
                for i in range(1, 1001):  # 循环1-1000次
                    if i % num == 0:
                        count += 1
                        print(count, "\t", i)
                        num_list.append(str(count) + "\t" + str(i) + "\n")  # 将结果写入到一个列表
                try:  # 判断是否写入错误
                    # 因为C盘要管理员所以改用D盘
                    with open(r"D:\{}的倍数.txt".format(num), "w", encoding='utf-8') as f:  # 用with打开文件赋给f
                        for s in num_list:
                            f.write(str(s))
                        f.close()
                    return False  # 终止循环
                except:
                    print("写入错误")
                    return True
            else:
                print("请输入1-100之间的数")
                return True
        else:
            print("请输入整数")
            return True
    except:
        print("请输入数字")
        return True


if __name__ == "__main__":
    while calculate():  # 利用循环重新输入
        calculate()
