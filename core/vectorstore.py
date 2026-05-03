from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 全局只加载一次Embedding模型，避免重复加载慢
_embeddings = None

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-zh-v1.5",
            model_kwargs={'device': 'cpu'}
        )
    return _embeddings

def add_documents(chunks):
    """把新文档加入向量数据库"""
    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=get_embeddings()
    )
    vectorstore.add_documents(chunks)
    return vectorstore

def get_vectorstore():
    """加载已有的向量数据库"""
    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=get_embeddings()
    )
