FROM python:alpine3.7

COPY . /app

WORKDIR /app

# RUN pip install -r requirements.txt
EXPOSE 3000

ADD 02_fibonacci_series.py /

CMD [ "python3", "./02_fibonacci_series.py" ]
