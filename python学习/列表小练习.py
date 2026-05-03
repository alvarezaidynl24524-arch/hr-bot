list1=[]
while True:
    result=input("请输入成绩:")
    if result == "结束":
        break
    else:
        list1.append(int(result))

if  list1:
    total_people =len(list1)
    max_core=max(list1)
    min_core = min(list1)
    total_score=sum(list1)
    excellent_people=0
    hege_people = 0

    for item in list1:
        if item>=60:
            hege_people+=1
        if item>=90:
            excellent_people+=1

    hege_lv=hege_people/total_people*100
    excellent_lv=excellent_people/total_people*100
    avg_score=total_score/total_people

    print(f"总人数为：{total_people}")
    print(f"最高分为：{max_core}")
    print(f"最低分为：{min_core}")
    print(f"合格人数为：{hege_people}")
    print(f"合格率为：{hege_lv:.1f}%")
    print(f"优秀人数为：{excellent_people}")
    print(f"优秀率为：{excellent_lv:.1f}%")
    print(f"平均分为：{avg_score:.1f}")
else:
    print("请回去输入成绩")