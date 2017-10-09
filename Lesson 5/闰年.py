print("闰年")
again = "y"
while again == "y":
    temp = input("输入年份")
    while temp.isdigit() == 0:
        temp = input("输入年份")
    year = int(temp)
    if (((year%4 == 0) and (year%100 != 0)) or (year%100 == 0))== True:
        print("是闰年")
    else:
        print("不是闰年")
    again = input("还玩吗？")
print("bye")
