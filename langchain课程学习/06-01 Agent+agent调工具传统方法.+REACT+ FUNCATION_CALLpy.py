# 1.导入相关包
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 2.定义搜索化工具
tools = [TavilySearchResults(max_results=1, tavily_api_key="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")]

# 3.自定义提示词模版
template = """Answer the following questions as best you can. You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)

# 4.定义LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

# 5.创建Agent对象
agent = create_react_agent(llm, tools, prompt)

# 6.创建AgentExecutor执行器
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# 7.测试
agent_executor.invoke({"input": "今天北京的天气怎么样？？"})