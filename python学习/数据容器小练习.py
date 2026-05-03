
students = [
    {
        'name': '张三',
        'scores': {'语文': 88, '数学': 92, '英语': 95}
    },
    {
        'name': '李四',
        'scores': {'语文': 75, '数学': 83, '英语': 80}
    },
    {
        'name': '王五',
        'scores': {'语文': 92, '数学': 95, '英语': 88}
    }
]
# def find_bext():
#
#     total = 0
#     excellent_students=[]
#     for item in students:
#         list1=item['scores'].values()
#         sum1=sum(list1)
#         if sum1>total:
#             total=sum1
#             excellent_students=[item['name']]
#         elif sum1==total:
#             excellent_students.append(item['name'])
#     print(f"最优秀的学生为：{excellent_students}，为 {total}分")
#
#
# find_bext()



#
# total = 0
# excellent_students=[]
# for item in students:
#     list1=item['scores'].values()
#     sum1=sum(list1)
#     if sum1>total:
#             total=sum1
#             excellent_students=[item['name']]
#     elif sum1==total:
#             excellent_students.append(item['name'])
# print(f"最优秀的学生为：{excellent_students}，为 {total}分")


# 练习三：评论内容
comment = '这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1：统计“好喝”出现次数
result1=comment.count("好喝")
print(result1)


# 需求2：将字符串中的“贵”替换为“略高”
result2=comment.replace("贵","略高")
print(result2)

# 需求3：是否包含“推荐”两个字
result3="推荐" in comment
print(result3)





