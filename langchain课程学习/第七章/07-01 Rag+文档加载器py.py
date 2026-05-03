# 1.导入相关依赖
from langchain_community.document_loaders import TextLoader

# 2.定义TextLoader对象，file_path=".txt的位置"
text_loader = TextLoader(file_path="asset/load/01-langchain-utf-8.txt", encoding="utf-8")

# 3.加载
docs = text_loader.load()  #返回List列表(Document对象)

# 4.打印
print(docs)