FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE $PORT

CMD ["flask", "run", "--host", "0.0.0.0", "--port", $PORT]