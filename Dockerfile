FROM python:3.6

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY web web/
COPY app.py app.py

CMD ["python3", "app.py"]
