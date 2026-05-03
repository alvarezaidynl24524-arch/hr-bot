import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="HR知识库助手",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 HR知识库智能助手")

# 左边栏：文档管理
with st.sidebar:
    st.header("📁 文档管理")

    # 上传文档
    uploaded_file = st.file_uploader(
        "上传公司文件",
        type=["pdf", "docx", "txt"],
        help="支持PDF、Word、TXT格式"
    )

    if uploaded_file and st.button("开始解析", type="primary"):
        with st.spinner("正在解析文档..."):
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
            response = requests.post(f"{BASE_URL}/upload", files=files)

            if response.status_code == 200:
                data = response.json()
                st.success(f"✅ 上传成功！切分了{data['chunks']}个片段")
            else:
                st.error(f"❌ 上传失败：{response.json()['detail']}")

    # 显示已有文档
    st.divider()
    st.subheader("已上传文档")
    try:
        resp = requests.get(f"{BASE_URL}/documents")
        docs = resp.json()["documents"]
        if docs:
            for doc in docs:
                st.text(f"📄 {doc}")
        else:
            st.info("还没有上传任何文档")
    except:
        st.warning("无法连接到后端服务")

# 右边主区域：问答
st.subheader("💬 提问")

# 用session_state保存对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 加这两行 ↓
if "history_pairs" not in st.session_state:
    st.session_state.history_pairs = []

# 显示历史对话
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 输入框
question = st.chat_input("请输入你的问题，例如：年假有几天？")

if question:
    # 显示用户问题
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    # 获取答案
    with st.chat_message("assistant"):
        with st.spinner("正在查询文档..."):
            result = None
            try:
                # 先用普通接口拿来源信息
                response = requests.post(
                    f"{BASE_URL}/ask",
                    json={"question": question,
                          "chat_history": st.session_state.get("history_pairs", [])}
                ).json()
                result=response
            except Exception as e:
                st.error(f"出错了：{str(e)}")
                result = None

        if result:
            # 流式显示答案
            def stream_answer():
                with requests.post(
                    f"{BASE_URL}/ask_stream",
                    json={"question": question,
                          "chat_history": st.session_state.get("history_pairs", [])},
                     stream=True
                        ) as r:
                            for chunk in r.iter_content(chunk_size=None, decode_unicode=True):
                                if chunk:
                                    yield chunk


            answer = st.write_stream(stream_answer())

            # 显示来源
            if result.get("sources"):
                with st.expander("📎 查看参考来源"):
                    for i, source in enumerate(result["sources"], 1):
                      st.caption(f"来源{i}（{source['source']}）：{source['content']}...")

                # 加这行 ↓
            st.session_state.history_pairs.append((question, answer))
            st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })
