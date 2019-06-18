FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt
CMD ["python3", "-m", "main"]