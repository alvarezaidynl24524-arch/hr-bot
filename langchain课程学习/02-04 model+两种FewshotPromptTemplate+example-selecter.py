from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
#1、创建示例集合
examples =[
{"input": "北京天气怎么样", "output": "北京市"},
{"input": "南京下雨吗", "output": "南京市"},
{"input": "武汉热吗", "output": "武汉市"}
]
#2、创建PromptTemplate实例
example_prompt = PromptTemplate.from_template(
template= "Input: {input}/nOutput:{output}"
)
#3、创建FewShotPromptTemplate实例
prompt = FewShotPromptTemplate(
examples=examples,
example_prompt=example_prompt,
suffix="Input:{input}/nOutput:",#要放在示例后面的提示模板字符串。
input_variables=["input"]
)#传入的变量
#4、调用
prompt = prompt.invoke({ "input": "长沙多少度"})


import os
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

#获取大模型
chat_model = ChatOpenAI(model="deepseek-v3.2")

#调用
response = chat_model.invoke(prompt)
print(response.content)