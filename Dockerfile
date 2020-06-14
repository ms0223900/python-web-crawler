FROM python:3.8.3-alpine3.12

WORKDIR /python-app

COPY . /python-app

RUN pip3 install -r requirements.txt

# ENTRYPOINT ["sh", "/python-app/install.sh"]

CMD ["python", "test-web-crawler.py"]