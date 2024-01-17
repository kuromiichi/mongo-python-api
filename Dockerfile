FROM python:alpine3.19

WORKDIR /app

COPY ./app .

RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]
