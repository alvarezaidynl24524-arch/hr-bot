FROM python:3.11-slim

WORKDIR /app

# 使用国内镜像加速 pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["echo", "请使用 docker-compose 启动"]