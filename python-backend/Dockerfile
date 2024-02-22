FROM --platform=arm64 python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]
# CMD ["flask","--app","main.py", "run"]
# CMD ["python", "-m", "flask", "--app", "./main.py"]
