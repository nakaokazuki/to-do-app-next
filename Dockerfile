FROM python:3.12-slim
# Python のログを見やすくする
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
# 依存インストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# アプリ本体をコピー
COPY . /app