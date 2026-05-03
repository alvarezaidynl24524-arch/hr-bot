age=int(input("请输入年龄："))
has_report=input("请输入是否提交报告（是/否）：")
level=int(input("请输入等级（1/2/3）："))
print("---------------------------结果如下------------------------------")
if  18<=age<=45:
    print("年龄在18到45之间√")
    if has_report=="是":
        print("能参加比赛√")
        if level==1:
            print(f"获得{level}会员礼物：T恤√")
        elif level == 2:
            print(f"获得{level}会员礼物：专业跑鞋√")
        else :
            print(f"获得{level}会员礼物：运动耳机√")

    else:
        print("不能能参加比赛")
else:
    print("不能参加比赛")