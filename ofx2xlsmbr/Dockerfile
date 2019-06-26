FROM python:3.7-alpine
COPY . /app/ofx2xlsmbr
WORKDIR /app
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r ofx2xlsmbr/requirements.txt
CMD ["python3", "-m", "main"]