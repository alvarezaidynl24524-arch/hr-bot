import os
from langchain_openai import ChatOpenAI
from .vectorstore import get_vectorstore
from FlagEmbedding import FlagReranker
import dotenv
#加载配置文件
dotenv.load_dotenv()
#1、获取对话模型：
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

def rewrite_query(question: str, llm) -> str:
    prompt = f"""
请把下面的问题改写成更适合在文档中检索的关键词形式，
只输出改写后的内容，不要解释。

原始问题：{question}
改写后："""
    return llm.invoke(prompt).content  # 加.content


def get_answer(question: str,chat_history: list = []) -> dict:
    vectorstore = get_vectorstore()
    llm = ChatOpenAI(model="deepseek-v3.2")

    # 先改写问题，再检索
    rewritten = rewrite_query(question, llm)
    print(f"改写后的检索词：{rewritten}")

    # 用改写后的问题去检索
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    relevant_docs = retriever.invoke(rewritten)

    # 用原始问题+检索结果让AI回答
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    # 把历史对话拼进去
    history_text = ""
    for human, ai in chat_history[-3:]:  # 只取最近3轮
        history_text += f"员工：{human}\nHR助手：{ai}\n\n"

    final_prompt = f"""
你是公司的HR助手，请根据下面的参考资料回答员工问题。
如果参考资料中没有相关内容，请回答"抱歉，文档中没有找到相关信息"。

{f"历史对话：{history_text}" if history_text else ""}

参考资料：
{context}

员工问题：{question}

回答："""

    answer = llm.invoke(final_prompt).content  # 加.content

    sources = [
        {
            "content": doc.page_content[:100],
            "source": doc.metadata.get("source", "未知文件")
        }
        for doc in relevant_docs
    ]

    return {"answer": answer, "sources": sources}


def get_answer_stream(question: str, chat_history: list = []):
    """流式版本，用生成器逐个yield token"""
    vectorstore = get_vectorstore()
    llm = ChatOpenAI(model="deepseek-v3.2", streaming=True)

    # 改写问题
    rewrite_llm = ChatOpenAI(model="deepseek-v3.2")
    rewritten = rewrite_query(question, rewrite_llm)
    print(f"改写后的检索词：{rewritten}")

    # 检索
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    relevant_docs = retriever.invoke(rewritten)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    # 历史对话
    history_text = ""
    for human, ai in chat_history[-3:]:
        history_text += f"员工：{human}\nHR助手：{ai}\n\n"

    final_prompt = f"""
你是公司的HR助手，请根据下面的参考资料回答员工问题。
如果参考资料中没有相关内容，请回答"抱歉，文档中没有找到相关信息"。

{f"历史对话：{history_text}" if history_text else ""}

参考资料：
{context}

员工问题：{question}

回答："""

    # 流式输出
    for chunk in llm.stream(final_prompt):
        yield chunk.content