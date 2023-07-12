from python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 8888

CMD ["python3","app.py"]

