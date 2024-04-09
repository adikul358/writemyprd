FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python3", "app.py"]