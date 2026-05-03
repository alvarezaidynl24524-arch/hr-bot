#1.导入相关依赖
from langchain_community.tools import MoveFileTool
from langchain_core.messages import HumanMessage
from langchain_core.utils.function_calling import convert_to_openai_function
import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 2.定义LLM模型
chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3.定义工具
tools = [MoveFileTool()]

# 4.这里需要将工具转换为openai函数，后续再将函数传入模型调用
functions = [convert_to_openai_function(t) for t in tools]

# print(functions[0])

# 5.提供大模型调用的消息列表
messages = [HumanMessage(content="将文件a移动到桌面")]

# 6.模型使用函数
response = chat_model.invoke(
    input = messages,
    functions=functions
)

print(response)