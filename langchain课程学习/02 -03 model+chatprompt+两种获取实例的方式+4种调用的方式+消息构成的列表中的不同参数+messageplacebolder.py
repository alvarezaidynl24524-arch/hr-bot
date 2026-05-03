

from langchain_openai import ChatOpenAI
import os
import dotenv
#加载配置文件
dotenv.load_dotenv()
#1、获取对话模型：
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")
chat_model = ChatOpenAI(
#必须要设置的3个参数
model="deepseek-v3.2",
#默认使用的是gpt-3.5-turbo模型
)
#2、通过Chat提示词模板，创建提示词
from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage

# 创建实例
chat_prompt_template = ChatPromptTemplate.from_messages(messages=[
("system", "You are a helpful assistant."),
MessagesPlaceholder("history"),
("human", "{question}")
]
)
response=chat_prompt_template.invoke({"history":[HumanMessage(content="1+2*3 = ?"),AIMessage(content="1+2*3=7")],
"question":"我刚才问题是什么？"})

response1=chat_model.invoke(response)
print(response1)