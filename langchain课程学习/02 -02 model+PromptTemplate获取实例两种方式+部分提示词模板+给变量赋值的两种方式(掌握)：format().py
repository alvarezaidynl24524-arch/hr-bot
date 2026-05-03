
from langchain.prompts import PromptTemplate
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
#定义多变量模板
template = PromptTemplate.from_template(
template="请评价{game}的优缺点，包括{aspect1}和{aspect2}。"
).partial(game="鸣潮")
#使用模板生成提示词
prompt_1 = template.invoke(input={"aspect1":"可玩性","aspect2":"用户体验"})
response=chat_model.invoke(prompt_1)
print(response.content)
