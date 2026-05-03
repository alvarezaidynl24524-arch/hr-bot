from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil, os
from core.loader import load_document
from core.vectorstore import add_documents
from fastapi.responses import StreamingResponse
app = FastAPI(title="HR知识库问答系统")

os.makedirs("./docs", exist_ok=True)


class QuestionRequest(BaseModel):
    question: str
    chat_history: list = []
@app.get("/")
def root():
    return {"message": "HR知识库系统运行中"}


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # 检查文件格式
    allowed = ['.pdf', '.docx', '.txt']
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed:
        raise HTTPException(status_code=400, detail="只支持PDF、Word、TXT格式")

    # 保存文件
    save_path = f"./docs/{file.filename}"
    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # 解析入库
    try:
        chunks = load_document(save_path)
        add_documents(chunks)
        return {
            "message": f"上传成功",
            "filename": file.filename,
            "chunks": len(chunks)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask")
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="问题不能为空")

    from core.qa import get_answer
    result = get_answer(request.question,request.chat_history)
    return result


@app.post("/ask_stream")
def ask_stream(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="问题不能为空")

    from core.qa import get_answer_stream

    def generate():
        for token in get_answer_stream(request.question, request.chat_history):
            yield token

    return StreamingResponse(generate(), media_type="text/plain")

@app.get("/documents")
def list_documents():
    """查看已上传的文档列表"""
    files = os.listdir("./docs")
    return {"documents": files}
