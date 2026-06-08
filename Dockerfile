# Модель: Метод Ньютона (5 семестр)
# Автор: Пташников Василь, група АІ-235

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .

# Порт за замовчуванням (Render сам підставить потрібний через $PORT)
EXPOSE 5000
CMD ["python", "main.py"]
