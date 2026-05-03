# 1.导入相关包

from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
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
# 2.创建LLM
llm = ChatOpenAI(model="deepseek-v3.2")

# 3.创建Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个与人类对话的机器人。"),
    MessagesPlaceholder(variable_name='history'),
    ("human", "问题: {question}")
])

# 4.创建Memory
memory = ConversationBufferMemory(return_messages=True)

# 5.创建LLMChain
llm_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)

# 6.调用LLMChain
res1 = llm_chain.invoke({"question": "中国首都在哪里？"})
print(res1, end="\n\n")

res2 = llm_chain.invoke({"question": "我刚才问的问题是什么？"})
print(res2, end="\n\n")