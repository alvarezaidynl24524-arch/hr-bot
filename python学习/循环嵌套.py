# day=1
# for day in range(1,31):
#     print(f"这是第{day}天")
#     for group in range(1,4):
#         print(f"这是第{group}组仰卧起坐")
#     print(f"第{day}任务已完成，明天继续！\n")
# print(f"恭喜！为期{day}天的健身计划完成！")


day=1
while day<31:
    print(f"这是第{day}天")
    group=1
    while group<4:
        print(f"这是第{group}组仰卧起坐")
        group=group+1
    print(f"第{day}任务已完成，明天继续！\n")
    day=day+1
print(f"恭喜！为期{day-1}天的健身计划完成！")
