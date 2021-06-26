FROM python:3.8.10-alpine3.13

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --update --no-cache gcc musl-dev libxslt-dev \
    && rm -rf /var/cache/apk/*

WORKDIR app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
