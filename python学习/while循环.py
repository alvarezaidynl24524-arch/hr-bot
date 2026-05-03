question="你是什么人？"
answer="我是友人A"
guess=""
while guess !=answer:
    guess=input(f"请回答问题，{question}：")
    if guess==answer:
        print("回答正确，友人A")
    else:
        print("回答错误")