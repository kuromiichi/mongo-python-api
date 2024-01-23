FROM python:alpine3.19

WORKDIR /app

COPY ./app .

COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD [ "flask", "--app=api.py", "run", "--host=0.0.0.0" ]
