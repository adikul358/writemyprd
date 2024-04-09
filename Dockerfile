FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV PORT 5000

EXPOSE $PORT

CMD ["flask", "run", "--host", "0.0.0.0", "--port", $PORT]