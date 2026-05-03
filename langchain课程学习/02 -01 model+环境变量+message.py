from langchain_core.messages import  SystemMessage ,HumanMessage
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
message=[SystemMessage(content="你是一个在ai方面权威的老师"),HumanMessage(content="cursor和vibe coding有什么区别？")]
# 2、调用模型

response =chat_model.invoke(message)

#3、查看响应的文本
# print(response.content)
print(response.content)