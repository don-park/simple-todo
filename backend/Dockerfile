FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 시작 스크립트 사용
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]