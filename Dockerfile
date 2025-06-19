# 使用官方 Python 3.11 slim 版
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 進去
COPY requirements.txt /app/

# 安裝依賴
RUN pip install -r requirements.txt

# 複製全部原始碼
COPY . /app

# 啟動 FastAPI 服務
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9001"]
