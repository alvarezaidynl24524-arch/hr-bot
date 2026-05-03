try:
    from langchain_classic.tools.retriever import create_retriever_tool
    print("✨ 终于找到了！就在 langchain_classic.tools.retriever")
except ImportError:
    print("❌ 路径 E 也失败了")
