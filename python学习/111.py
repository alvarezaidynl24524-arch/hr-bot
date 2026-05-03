
question1, answer1="你是谁","我是友人A"
question2, answer2="我走进你的心房了吗","是的"
question3, answer3="下次还会再见面吗","是的"
is_playing = True
max_tries = 3
total_levels=3
for level in range(1,total_levels+1):
    print(f'********🎯第{level}关********')
    if level==1:
        question, answer=question1, answer1
    elif level==2:
        question, answer=question2, answer2
    else:
        question, answer=question3, answer3
    try1 = 1
    while try1 <= max_tries:
        user_input=input(question)
        if  user_input == answer:
            print("回答成功")
            break
        elif user_input == '':
            print('⚠️您的输入为空，请重新作答！\n')
            continue
        elif user_input == "q":
            print('您已经退出\n')
            is_playing = False
            break
        else:
            leave = max_tries - try1
            if leave>0:
                print(f"还有{leave}次机会")
                try1+= 1
                continue
            else:
                print(f'😢挑战失败，本题的正确答案是：{answer}，游戏结束！')
                is_playing = False
                break
    if not is_playing:
        break
    # 如果到了这里，is_playing的值依然为True，那就意味着用户已经通关了！
if is_playing:
    print('🎉🎉🎉恭喜您！全部通关！🎉🎉🎉')