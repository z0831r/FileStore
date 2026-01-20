FROM python:3.10-slim

WORKDIR /app

# 设置时区为上海，方便看日志时间
RUN apt-get update && apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
