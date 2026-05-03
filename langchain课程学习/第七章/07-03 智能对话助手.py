import os
from langchain_community.tools.tavily_search import TavilySearchResults

# 定义 TAVILY_KEY 密钥
os.environ["TAVILY_API_KEY"] = "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"
# 查询 Tavily 搜索 API
search = TavilySearchResults(max_results=1)
# 执行查询
res = search.invoke("今天上海天气怎么样")
print(res)

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import dotenv
dotenv.load_dotenv()

# 1. 提供一个大模型
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

embedding_model = OpenAIEmbeddings()

# 2. 加载HTML内容为一个文档对象
loader = WebBaseLoader("https://zh.wikipedia.org/wiki/%E7%8C%AB")
docs = loader.load()
#print(docs)

# 3. 分割文档
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

documents = splitter.split_documents(docs)

# 4. 向量化 得到向量数据库对象
vector = FAISS.from_documents(documents, embedding_model)

# 5. 创建检索器
retriever = vector.as_retriever()

# 测试检索结果
#print(retriever.invoke("猫的特征")[0])

from langchain_classic.tools.retriever import create_retriever_tool


# 创建一个工具来检索文档
retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="wiki_search",
    description="搜索维基百科",
)

tools = [search, retriever_tool]

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# 获取大模型
model = ChatOpenAI(model="gpt-4o-mini")

# 模型绑定工具
model_with_tools = model.bind_tools(tools)

# 根据输入自动调用工具
messages = [HumanMessage(content="今天上海天气怎么样")]
response = model_with_tools.invoke(messages)
print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")

from langchainhub import Client


# 1. 使用 pull_prompt 替代 pull
prompt = Client().pull_prompt("hwchase17/openai-functions-agent")

# 2. 在打印之前，我们先检查一下它的类型，确保它不是普通字符串
print(f"Prompt 类型是: {type(prompt)}")

# 3. 再尝试访问 messages
print(prompt.messages)


print(prompt.messages)

from langchain_classic.agents import create_tool_calling_agent
from langchain_classic.agents import AgentExecutor


# 创建Agent对象
agent = create_tool_calling_agent(model, tools, prompt)

# 创建AgentExecutor对象
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}

# 调取指定session_id对应的memory
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

agent_with_chat_history = RunnableWithMessageHistory(
    runnable=agent_executor,
    get_session_history=get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

response = agent_with_chat_history.invoke(
    {"input": "Hi, 我的名字是Cyber"},
    config={"configurable": {"session_id": "123"}},
)
print(response)

response = agent_with_chat_history.invoke(
    {"input": "我叫什么名字?"},
    config={"configurable": {"session_id": "123"}},
)
print(response)