import os
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

import dotenv
#加载配置文件
dotenv.load_dotenv()
#1、获取对话模型：
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"


# ========== 第一步：加载文档 ==========
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


# ========== 第二步：切片 ==========
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,  # 每块最多200个字
        chunk_overlap=20,  # 块之间重叠20个字，防止内容被截断
    )
    chunks = splitter.create_documents([text])
    print(f"文档被切成了 {len(chunks)} 块")
    return chunks


# ========== 第三步：向量化存储 ==========
def create_vectorstore(chunks):
    print("正在加载Embedding模型，第一次会下载，请等待...")
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-zh-v1.5",
        model_kwargs={'device': 'cpu'}
    )
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    print("向量数据库创建成功！")
    return vectorstore


# ========== 第四步：构建问答链 ==========
def build_qa_chain(vectorstore):
    llm = ChatOpenAI(model="deepseek-v3.2")

    # 自定义Prompt，告诉AI怎么回答
    prompt_template = """
你是公司的HR助手，请根据下面的参考资料回答员工问题。
如果参考资料中没有答案，就说"抱歉，文档中没有找到相关信息"。
不要编造任何内容。

参考资料：
{context}

员工问题：{question}

回答："""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}  # 每次检索最相关的3块内容
        ),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
    return qa_chain


# ========== 主程序 ==========
if __name__ == "__main__":
    # 加载并处理文档
    text = load_text("./docs/test.txt")
    chunks = split_text(text)
    vectorstore = create_vectorstore(chunks)
    qa_chain = build_qa_chain(vectorstore)

    # 开始问答
    print("\n=== HR助手已就绪，输入q退出 ===\n")
    while True:
        question = input("你的问题：")
        if question == 'q':
            break

        result = qa_chain.invoke({"query": question})
        print(f"\n答案：{result['result']}")
        print(f"\n--- 参考来源 ---")
        for doc in result['source_documents']:
            print(f"  · {doc.page_content[:50]}...")
        print()
